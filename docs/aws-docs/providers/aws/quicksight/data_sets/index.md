---
title: data_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sets
  - quicksight
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>data_sets</code> in a region or to create or delete a <code>data_sets</code> resource, use <code>data_set</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::DataSet Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.data_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_set_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
aws_account_id,
data_set_id
FROM aws.quicksight.data_sets
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "AwsAccountId": "{{ AwsAccountId }}",
 "ColumnGroups": [
  {
   "GeoSpatialColumnGroup": {
    "Columns": [
     "{{ Columns[0] }}"
    ],
    "CountryCode": "{{ CountryCode }}",
    "Name": "{{ Name }}"
   }
  }
 ],
 "ColumnLevelPermissionRules": [
  {
   "ColumnNames": [
    "{{ ColumnNames[0] }}"
   ],
   "Principals": [
    "{{ Principals[0] }}"
   ]
  }
 ],
 "DataSetId": "{{ DataSetId }}",
 "DatasetParameters": [
  {
   "StringDatasetParameter": {
    "Id": "{{ Id }}",
    "Name": "{{ Name }}",
    "ValueType": "{{ ValueType }}",
    "DefaultValues": {
     "StaticValues": [
      "{{ StaticValues[0] }}"
     ]
    }
   },
   "DecimalDatasetParameter": {
    "Id": null,
    "Name": null,
    "ValueType": null,
    "DefaultValues": {
     "StaticValues": [
      null
     ]
    }
   },
   "IntegerDatasetParameter": {
    "Id": null,
    "Name": null,
    "ValueType": null,
    "DefaultValues": {
     "StaticValues": [
      null
     ]
    }
   },
   "DateTimeDatasetParameter": {
    "Id": null,
    "Name": null,
    "ValueType": null,
    "TimeGranularity": "{{ TimeGranularity }}",
    "DefaultValues": {
     "StaticValues": [
      "{{ StaticValues[0] }}"
     ]
    }
   }
  }
 ],
 "FieldFolders": {},
 "ImportMode": "{{ ImportMode }}",
 "LogicalTableMap": {},
 "Name": "{{ Name }}",
 "Permissions": [
  {
   "Principal": "{{ Principal }}",
   "Actions": [
    "{{ Actions[0] }}"
   ]
  }
 ],
 "PhysicalTableMap": {},
 "RowLevelPermissionDataSet": {
  "Arn": "{{ Arn }}",
  "Namespace": "{{ Namespace }}",
  "PermissionPolicy": "{{ PermissionPolicy }}",
  "FormatVersion": "{{ FormatVersion }}",
  "Status": "{{ Status }}"
 },
 "RowLevelPermissionTagConfiguration": {
  "Status": null,
  "TagRules": [
   {
    "ColumnName": "{{ ColumnName }}",
    "TagKey": "{{ TagKey }}",
    "MatchAllValue": "{{ MatchAllValue }}",
    "TagMultiValueDelimiter": "{{ TagMultiValueDelimiter }}"
   }
  ],
  "TagRuleConfigurations": [
   [
    "{{ 0[0] }}"
   ]
  ]
 },
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "IngestionWaitPolicy": {
  "WaitForSpiceIngestion": "{{ WaitForSpiceIngestion }}",
  "IngestionWaitTimeInHours": null
 },
 "DataSetUsageConfiguration": {
  "DisableUseAsDirectQuerySource": "{{ DisableUseAsDirectQuerySource }}",
  "DisableUseAsImportedSource": "{{ DisableUseAsImportedSource }}"
 },
 "DataSetRefreshProperties": {
  "RefreshConfiguration": {
   "IncrementalRefresh": {
    "LookbackWindow": {
     "ColumnName": "{{ ColumnName }}",
     "Size": null,
     "SizeUnit": "{{ SizeUnit }}"
    }
   }
  }
 }
}
>>>
--required properties only
INSERT INTO aws.quicksight.data_sets (
 AwsAccountId,
 ColumnGroups,
 ColumnLevelPermissionRules,
 DataSetId,
 DatasetParameters,
 FieldFolders,
 ImportMode,
 LogicalTableMap,
 Name,
 Permissions,
 PhysicalTableMap,
 RowLevelPermissionDataSet,
 RowLevelPermissionTagConfiguration,
 Tags,
 IngestionWaitPolicy,
 DataSetUsageConfiguration,
 DataSetRefreshProperties,
 region
)
SELECT 
{{ .AwsAccountId }},
 {{ .ColumnGroups }},
 {{ .ColumnLevelPermissionRules }},
 {{ .DataSetId }},
 {{ .DatasetParameters }},
 {{ .FieldFolders }},
 {{ .ImportMode }},
 {{ .LogicalTableMap }},
 {{ .Name }},
 {{ .Permissions }},
 {{ .PhysicalTableMap }},
 {{ .RowLevelPermissionDataSet }},
 {{ .RowLevelPermissionTagConfiguration }},
 {{ .Tags }},
 {{ .IngestionWaitPolicy }},
 {{ .DataSetUsageConfiguration }},
 {{ .DataSetRefreshProperties }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AwsAccountId": "{{ AwsAccountId }}",
 "ColumnGroups": [
  {
   "GeoSpatialColumnGroup": {
    "Columns": [
     "{{ Columns[0] }}"
    ],
    "CountryCode": "{{ CountryCode }}",
    "Name": "{{ Name }}"
   }
  }
 ],
 "ColumnLevelPermissionRules": [
  {
   "ColumnNames": [
    "{{ ColumnNames[0] }}"
   ],
   "Principals": [
    "{{ Principals[0] }}"
   ]
  }
 ],
 "DataSetId": "{{ DataSetId }}",
 "DatasetParameters": [
  {
   "StringDatasetParameter": {
    "Id": "{{ Id }}",
    "Name": "{{ Name }}",
    "ValueType": "{{ ValueType }}",
    "DefaultValues": {
     "StaticValues": [
      "{{ StaticValues[0] }}"
     ]
    }
   },
   "DecimalDatasetParameter": {
    "Id": null,
    "Name": null,
    "ValueType": null,
    "DefaultValues": {
     "StaticValues": [
      null
     ]
    }
   },
   "IntegerDatasetParameter": {
    "Id": null,
    "Name": null,
    "ValueType": null,
    "DefaultValues": {
     "StaticValues": [
      null
     ]
    }
   },
   "DateTimeDatasetParameter": {
    "Id": null,
    "Name": null,
    "ValueType": null,
    "TimeGranularity": "{{ TimeGranularity }}",
    "DefaultValues": {
     "StaticValues": [
      "{{ StaticValues[0] }}"
     ]
    }
   }
  }
 ],
 "FieldFolders": {},
 "ImportMode": "{{ ImportMode }}",
 "LogicalTableMap": {},
 "Name": "{{ Name }}",
 "Permissions": [
  {
   "Principal": "{{ Principal }}",
   "Actions": [
    "{{ Actions[0] }}"
   ]
  }
 ],
 "PhysicalTableMap": {},
 "RowLevelPermissionDataSet": {
  "Arn": "{{ Arn }}",
  "Namespace": "{{ Namespace }}",
  "PermissionPolicy": "{{ PermissionPolicy }}",
  "FormatVersion": "{{ FormatVersion }}",
  "Status": "{{ Status }}"
 },
 "RowLevelPermissionTagConfiguration": {
  "Status": null,
  "TagRules": [
   {
    "ColumnName": "{{ ColumnName }}",
    "TagKey": "{{ TagKey }}",
    "MatchAllValue": "{{ MatchAllValue }}",
    "TagMultiValueDelimiter": "{{ TagMultiValueDelimiter }}"
   }
  ],
  "TagRuleConfigurations": [
   [
    "{{ 0[0] }}"
   ]
  ]
 },
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "IngestionWaitPolicy": {
  "WaitForSpiceIngestion": "{{ WaitForSpiceIngestion }}",
  "IngestionWaitTimeInHours": null
 },
 "DataSetUsageConfiguration": {
  "DisableUseAsDirectQuerySource": "{{ DisableUseAsDirectQuerySource }}",
  "DisableUseAsImportedSource": "{{ DisableUseAsImportedSource }}"
 },
 "DataSetRefreshProperties": {
  "RefreshConfiguration": {
   "IncrementalRefresh": {
    "LookbackWindow": {
     "ColumnName": "{{ ColumnName }}",
     "Size": null,
     "SizeUnit": "{{ SizeUnit }}"
    }
   }
  }
 }
}
>>>
--all properties
INSERT INTO aws.quicksight.data_sets (
 AwsAccountId,
 ColumnGroups,
 ColumnLevelPermissionRules,
 DataSetId,
 DatasetParameters,
 FieldFolders,
 ImportMode,
 LogicalTableMap,
 Name,
 Permissions,
 PhysicalTableMap,
 RowLevelPermissionDataSet,
 RowLevelPermissionTagConfiguration,
 Tags,
 IngestionWaitPolicy,
 DataSetUsageConfiguration,
 DataSetRefreshProperties,
 region
)
SELECT 
 {{ .AwsAccountId }},
 {{ .ColumnGroups }},
 {{ .ColumnLevelPermissionRules }},
 {{ .DataSetId }},
 {{ .DatasetParameters }},
 {{ .FieldFolders }},
 {{ .ImportMode }},
 {{ .LogicalTableMap }},
 {{ .Name }},
 {{ .Permissions }},
 {{ .PhysicalTableMap }},
 {{ .RowLevelPermissionDataSet }},
 {{ .RowLevelPermissionTagConfiguration }},
 {{ .Tags }},
 {{ .IngestionWaitPolicy }},
 {{ .DataSetUsageConfiguration }},
 {{ .DataSetRefreshProperties }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.quicksight.data_sets
WHERE data__Identifier = '<AwsAccountId|DataSetId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_sets</code> resource, the following permissions are required:

### Create
```json
quicksight:DescribeDataSet,
quicksight:DescribeDataSetPermissions,
quicksight:DescribeIngestion,
quicksight:ListIngestions,
quicksight:CreateDataSet,
quicksight:PassDataSource,
quicksight:PassDataSet,
quicksight:TagResource,
quicksight:ListTagsForResource,
quicksight:DescribeDataSetRefreshProperties,
quicksight:PutDataSetRefreshProperties
```

### Delete
```json
quicksight:DescribeDataSet,
quicksight:DeleteDataSet,
quicksight:ListTagsForResource,
quicksight:DescribeIngestion,
quicksight:DeleteDataSetRefreshProperties,
quicksight:DescribeDataSetRefreshProperties
```

### List
```json
quicksight:DescribeDataSet,
quicksight:ListDataSets
```

