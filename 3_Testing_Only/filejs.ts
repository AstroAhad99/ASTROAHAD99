export interface JsonfileJSON {
    name:    TypeID;
    tagType: TypeID;
    tags:    JsonfileJSONTag[];
}

export interface JsonfileJSONTag {
    name:    string;
    typeId:  TypeID;
    tagType: TagType;
    tags:    PurpleTag[];
}

export enum TagType {
    AtomicTag = "AtomicTag",
    UdtInstance = "UdtInstance",
}

export interface PurpleTag {
    name:    Name;
    tagType: TagType;
    tags?:   FluffyTag[];
    value?:  number;
}

export enum Name {
    The1_Fork = "1_Fork",
    The2_Coordinates = "2_Coordinates",
    The3_String = "3_String",
}

export interface FluffyTag {
    name:    string;
    tagType: TagType;
}

export enum TypeID {
    MissionsMainMissionMem = "Missions/Main/Mission Mem",
}
