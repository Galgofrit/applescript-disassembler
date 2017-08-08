opcodes = '''Equal
NotEqual
GreaterThan
GreaterThanOrEqual
LessThan
LessThanOrEqual
StartsWith
EndsWith
Contains
And
Or
Not
MessageSend
MakeList
MakeRecord
Return
Continue
ObjectAliasQuote
Tell
Consider
ErrorHandler
Error
Exit
LinkRepeat
RepeatNTimes
RepeatWhile
RepeatUntil
RepeatInCollection
RepeatInRange
TestIf
Add
Subtract
Multiply
Divide
Quotient
Remainder
Power
Concatenate
Coerce
Negate
GetData
PushMe
PushIt
PositionalMessageSend
MakeObjectAlias
MakeObjectAlias
MakeObjectAlias
MakeObjectAlias
MakeObjectAlias
MakeObjectAlias
MakeObjectAlias
MakeObjectAlias
MakeObjectAlias
MakeObjectAlias
MakeObjectAlias
MakeObjectAlias
MakeComp
MakeComp
MakeComp
MakeComp
MakeComp
MakeComp
MakeComp
MakeComp
MakeComp
MakeComp
MakeComp
MakeComp
MakeComp
GetData
SetData
CopyData
Undefined
Undefined
PositionalContinue
DefineActor
DefineProcedure
DefineClosure
DefineProperty
StoreResult
GetResult
Clone
Of
EndDefineActor
EndOf
EndTell
EndConsider
EndErrorHandler
HandleError
Jump
Pop
Dup
GCSwap
PushVariableExtended
PopVariableExtended
PushGlobalExtended
PopGlobalExtended
PushLiteralExtended
PushParentVariable
PopParentVariable
PushNext
PushTrue
PushFalse
PushEmpty
PushUndefined
PushMinus1
Push0
Push1
Push2
Push3
BeginTimeout
EndTimeout
BeginTransaction
EndTransaction
Undefined
Undefined
Undefined
MatchLiteral
MakeVector
None
None
None
None
None
None
None
None
None
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
Undefined
PushVariable
PushVariable
PushVariable
PushVariable
PushVariable
PushVariable
PushVariable
PushVariable
PushVariable
PushVariable
PushVariable
PushVariable
PushVariable
PushVariable
PushVariable
PushVariable
PopVariable
PopVariable
PopVariable
PopVariable
PopVariable
PopVariable
PopVariable
PopVariable
PopVariable
PopVariable
PopVariable
PopVariable
PopVariable
PopVariable
PopVariable
PopVariable
PushGlobal
PushGlobal
PushGlobal
PushGlobal
PushGlobal
PushGlobal
PushGlobal
PushGlobal
PushGlobal
PushGlobal
PushGlobal
PushGlobal
PushGlobal
PushGlobal
PushGlobal
PushGlobal
PopGlobal
PopGlobal
PopGlobal
PopGlobal
PopGlobal
PopGlobal
PopGlobal
PopGlobal
PopGlobal
PopGlobal
PopGlobal
PopGlobal
PopGlobal
PopGlobal
PopGlobal
PopGlobal
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral
PushLiteral'''.split('\n')

def getSizeByIndex(x):
    if x in [4,
    14,
    18,
    21,
    22,
    23,
    26,
    28,
    29,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    45,
    58,
    59,
    83,
    102,
    103,
    122]:
      return 3;
    if x in [15,
    53,
    55,
    73,
    80,
    81,
    82,
    88,
    108,
    120,
    124]:
      return 6
    if x in [16,
    17,
    89]:
      return 8
    if x in [19]:
      return 1;
    if x in [20,
    30,
    31,
    44,
    177]:
      return 2;
    if x in [24,
    49,
    50,
    51,
    56,
    57,
    60,
    72,
    74,
    75,
    76,
    77,
    78,
    84,
    100,
    101,
    107,
    109,
    111,
    112,
    113,
    118,
    123]:
      return 4;
    if x in [25,
    27,
    52,
    54,
    61,
    62,
    63,
    64,
    65,
    66,
    67,
    68,
    69,
    70,
    71,
    79,
    85,
    86,
    87,
    91,
    92,
    93,
    94,
    95,
    96,
    97,
    98,
    99,
    104,
    105,
    106,
    110,
    114,
    115,
    116,
    117,
    119]:
      return 5;
    if x in [90]:
      return 7;

ConstMap = {
    0x7A2: 'true',
    0x792: 'false'
}

comments = {
    21: 'GetProperty',
    21 + 1: 'GetEvery',
    21 + 2: 'GetSome',
    21 + 3: 'GetIndexed (item A of B)',
    21 + 4: 'GetKeyFrom',
    21 + 6: 'GetRange',
    21 + 9: 'GetPositionBeginning',
    21 + 10: 'GetPositionEnd',
    21 + 11: 'GetMiddle'
}

if __name__ == '__main__':
    for i in range(256):
        if opcodes[i] == 'None':
            opcodes[i] = ''
        print '%02x' % i, opcodes[i]