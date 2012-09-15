import API_request_pb2
import API_response_pb2
import API_program_pb2
import muf_type_manager

def api_send(muf_env, message):
    transmission = API_program_pb2.ResponseStatus()
    transmission.status_code = 1
    transmission.request_message.CopyFrom(message)
    print transmission
    muf_env["api"].send(transmission.SerializeToString())
    return muf_env["api"].recv()

def set_player(muf_env, message):
    """Sets the DBREF of the requesting player in the Protobuf."""
    message.player_ref.site_id = muf_env['site_id']
    message.player_ref.object_id = muf_env['priv_user'].get_dbref()

def get_props(muf_env, object_id, prop_name):
    request = API_request_pb2.RequestMessage()
    request.type = API_request_pb2.GET_PROPS
    set_player(muf_env,request)
    request.request_get_props_fields.object_id.site_id = muf_env['site_id']
    request.request_get_props_fields.object_id.object_id = object_id.get_dbref()
    request.request_get_props_fields.propnames.append("_MUF_TYPE_TABLE/" + prop_name)
    request.request_get_props_fields.propnames.append(prop_name)
    response = API_response_pb2.APIResponse()
    response.ParseFromString(api_send(muf_env,request))
    props = list(response.list_of_props_fields.props)
    if len(props) == 2:
        prop_val=muf_type_manager.restore_typed_value(muf_env,props.pop(), props.pop())
        return prop_val
    elif len(props) == 1:
        return props.pop()
    else:
        return 0

def set_props(muf_env, object_id, prop_name, prop_val):
    request = API_request_pb2.RequestMessage()
    request.type = API_request_pb2.SET_PROPS
    set_player(muf_env,request)
    request.request_set_props_fields.object_id.site_id = muf_env['site_id']
    request.request_set_props_fields.object_id.object_id=object_id.get_dbref()
    dict_item = request.request_set_props_fields.props.add()
    dict_item.key = "_MUF_TYPE_TABLE/" + prop_name
    dict_item.value = muf_type_manager.save_type_value(muf_env,prop_val)
    dict_item = request.request_set_props_fields.props.add()
    dict_item.key = prop_name
    dict_item.value = muf_type_manager.stringer(muf_env,prop_val)
    api_send(muf_env, request) # No checks for now. We'll add them once we know this all works.

def notify_objects(muf_env, object_id, message):
    request = API_request_pb2.RequestMessage()
    request.type = API_request_pb2.NOTIFY_OBJECTS
    set_player(muf_env,request)
    target = request.request_notify_objects_fields.object_id.add()
    target.site_id = muf_env['site_id']
    target.object_id = object_id.get_dbref()
    request.request_notify_objects_fields.message = message
    api_send(muf_env,request)

