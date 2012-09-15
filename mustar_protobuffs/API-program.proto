package MustarAPI;

// This package is for the programmatic section of the API.

import "ref.proto";
import "API-request.proto";
import "API-response.proto";

enum CommandType {
    INIT = 0;
    EXECUTE = 1;
    KILL = 2;
    SIGNAL = 3;
    DIE = 4; // Shut down the interpreter Daemon.
    STATUS = 5; // Ask for a status report of the interpreter-- all PIDs, their owners, etc.
}

// The different types of instructions we can send the interpreter.
message CommandMessage {
    required CommandType type = 1;
    optional InitCommand init_command_fields = 2;
    optional ExecuteCommand execute_command_fields = 3;
    optional KillCommand kill_command_fields = 4;
    optional SignalCommand signal_command_fields = 5;
}


// Key value pair. Protobufs won't check for duplicates.
// You should accept the last given entry of a duplicate as overriding.
message dictionary {
    required string key = 1;
    required string value = 2;
}

// Request that the program be compiled into memory in preperation
// for execution. pid is the process ID the new program should have.
// If pid is not provided, compilation will occur with a status message
// returned, but the muf object will be deleted right after. This is useful
// for syntax checks.
// instrlimit is the instruction limit that is imposed on a new process.
// If the instruction count goes beyond this, the program should die.
message InitCommand {
    required string raw_code = 1;
    required int32 pid = 2;
    required int32 site_id = 3;
    optional int32 instr_limit = 4;
    required MuStarDatabase.Ref me = 5;
    required MuStarDatabase.Ref loc = 6;
    required MuStarDatabase.Ref trigger = 7;
    required string command = 8;
    required int32 m_level = 9;
    required MuStarDatabase.Ref prog = 10;
    required MuStarDatabase.Ref room = 11;
    required MuStarDatabase.Ref user = 12;
    required MuStarDatabase.Ref priv_user = 13;
    optional int32 debug = 14;
}

// Execute a particular process ID. Instruction count
// is how many instructions it is to process before sleeping.
// Response message: ResponseStatus
message ExecuteCommand {
    required int32 pid = 1;
    required int32 instruction_count = 2;
}

// Force a process to die.
// Reponse message: ResponseStatus
message KillCommand {
    required int32 pid = 1;
}

// For sending process signals. This probably won't be used for a little while.
// Response message: ResponseStatus
message SignalCommand {
    required string signal = 1;
    optional string data = 2;
}

// Used by the interpreter to pass messages back to the core.
// This is not the message for a general status request response.
// I'll write that later.
// 0 is 'finished timeslice', 1 is 'api request', 2 is 'Program complete'.
// Others are not yet defined.
message ResponseStatus {
    required int32 status_code = 1;
    optional string status_message = 2;
    optional RequestMessage request_message = 3;
    optional APIResponse api_reponse = 4;
}
