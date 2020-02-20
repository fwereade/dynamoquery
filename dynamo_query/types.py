from typing import Dict, Callable, Any, Set, TypeVar, TYPE_CHECKING

from typing_extensions import Literal

from dynamo_query.data_table import DataTable

if TYPE_CHECKING:
    from mypy_boto3.dynamodb.service_resource import Table
    from mypy_boto3.dynamodb.client import DynamoDBClient
    from mypy_boto3.dynamodb.type_defs import (
        ClientGetItemResponseTypeDef,
        ClientUpdateItemResponseTypeDef,
        ClientDeleteItemResponseTypeDef,
        ClientQueryResponseTypeDef,
        ClientScanResponseTypeDef,
        ClientBatchGetItemResponseTypeDef,
        ClientBatchWriteItemResponseTypeDef,
        ClientCreateTableGlobalSecondaryIndexesTypeDef,
        ClientCreateTableLocalSecondaryIndexesTypeDef,
        ClientCreateTableGlobalSecondaryIndexesKeySchemaTypeDef,
        ClientCreateTableLocalSecondaryIndexesKeySchemaTypeDef,
        ClientCreateTableKeySchemaTypeDef,
        ClientCreateTableAttributeDefinitionsTypeDef,
    )

else:
    Table = object
    DynamoDBClient = object
    BaseExpression = object
    ClientGetItemResponseTypeDef = object
    ClientUpdateItemResponseTypeDef = object
    ClientDeleteItemResponseTypeDef = object
    ClientQueryResponseTypeDef = object
    ClientScanResponseTypeDef = object
    ClientBatchGetItemResponseTypeDef = object
    ClientBatchWriteItemResponseTypeDef = object
    ClientCreateTableGlobalSecondaryIndexesTypeDef = object
    ClientCreateTableLocalSecondaryIndexesTypeDef = object
    ClientCreateTableGlobalSecondaryIndexesKeySchemaTypeDef = object
    ClientCreateTableLocalSecondaryIndexesKeySchemaTypeDef = object
    ClientCreateTableKeySchemaTypeDef = object
    ClientCreateTableAttributeDefinitionsTypeDef = object


BaseExpression = TypeVar("BaseExpression")
ExpressionMap = Dict[str, BaseExpression]
FormatDict = Dict[str, Any]
TableKeys = Set[str]
QueryMethod = Callable[[DataTable], DataTable]
ExclusiveStartKey = Dict[str, Any]
ConditionExpressionOperatorStr = Literal[
    "=",
    "<>",
    "IN",
    ">",
    "<",
    ">=",
    "<=",
    "begins_with",
    "attribute_exists",
    "attribute_not_exists",
    "BETWEEN",
    "contains",
]
ConditionExpressionJoinOperatorStr = Literal[
    "AND", "OR",
]

ReturnValues = Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"]
ReturnItemCollectionMetrics = Literal["NONE", "SIZE"]
ReturnConsumedCapacity = Literal["INDEXES", "TOTAL", "NONE"]
