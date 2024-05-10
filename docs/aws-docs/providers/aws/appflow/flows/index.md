---
title: flows
hide_title: false
hide_table_of_contents: false
keywords:
  - flows
  - appflow
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


Used to retrieve a list of <code>flows</code> in a region or to create or delete a <code>flows</code> resource, use <code>flow</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::AppFlow::Flow.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appflow.flows" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="flow_name" /></td><td><code>string</code></td><td>Name of the flow.</td></tr>
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
flow_name
FROM aws.appflow.flows
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
 "FlowName": "{{ FlowName }}",
 "TriggerConfig": {
  "TriggerType": "{{ TriggerType }}",
  "TriggerProperties": {
   "ScheduleExpression": "{{ ScheduleExpression }}",
   "DataPullMode": "{{ DataPullMode }}",
   "ScheduleStartTime": null,
   "ScheduleEndTime": null,
   "FirstExecutionFrom": null,
   "TimeZone": "{{ TimeZone }}",
   "ScheduleOffset": null,
   "FlowErrorDeactivationThreshold": "{{ FlowErrorDeactivationThreshold }}"
  }
 },
 "SourceFlowConfig": {
  "ConnectorType": "{{ ConnectorType }}",
  "ApiVersion": "{{ ApiVersion }}",
  "ConnectorProfileName": "{{ ConnectorProfileName }}",
  "SourceConnectorProperties": {
   "Amplitude": {
    "Object": "{{ Object }}"
   },
   "Datadog": {
    "Object": null
   },
   "Dynatrace": {
    "Object": null
   },
   "GoogleAnalytics": {
    "Object": null
   },
   "InforNexus": {
    "Object": null
   },
   "Marketo": {
    "Object": null
   },
   "S3": {
    "BucketName": "{{ BucketName }}",
    "BucketPrefix": "{{ BucketPrefix }}",
    "S3InputFormatConfig": {
     "S3InputFileType": "{{ S3InputFileType }}"
    }
   },
   "SAPOData": {
    "ObjectPath": null,
    "parallelismConfig": {
     "maxParallelism": "{{ maxParallelism }}"
    },
    "paginationConfig": {
     "maxPageSize": "{{ maxPageSize }}"
    }
   },
   "Salesforce": {
    "Object": null,
    "EnableDynamicFieldUpdate": "{{ EnableDynamicFieldUpdate }}",
    "IncludeDeletedRecords": "{{ IncludeDeletedRecords }}",
    "DataTransferApi": "{{ DataTransferApi }}"
   },
   "Pardot": {
    "Object": null
   },
   "ServiceNow": {
    "Object": null
   },
   "Singular": {
    "Object": null
   },
   "Slack": {
    "Object": null
   },
   "Trendmicro": {
    "Object": null
   },
   "Veeva": {
    "Object": null,
    "DocumentType": "{{ DocumentType }}",
    "IncludeSourceFiles": "{{ IncludeSourceFiles }}",
    "IncludeRenditions": "{{ IncludeRenditions }}",
    "IncludeAllVersions": "{{ IncludeAllVersions }}"
   },
   "Zendesk": {
    "Object": null
   },
   "CustomConnector": {
    "EntityName": "{{ EntityName }}",
    "CustomProperties": {},
    "DataTransferApi": {
     "Name": "{{ Name }}",
     "Type": "{{ Type }}"
    }
   }
  },
  "IncrementalPullConfig": {
   "DatetimeTypeFieldName": "{{ DatetimeTypeFieldName }}"
  }
 },
 "DestinationFlowConfigList": [
  {
   "ConnectorType": null,
   "ApiVersion": null,
   "ConnectorProfileName": null,
   "DestinationConnectorProperties": {
    "Redshift": {
     "Object": null,
     "IntermediateBucketName": null,
     "BucketPrefix": null,
     "ErrorHandlingConfig": {
      "FailOnFirstError": "{{ FailOnFirstError }}",
      "BucketPrefix": null,
      "BucketName": null
     }
    },
    "S3": {
     "BucketName": null,
     "BucketPrefix": null,
     "S3OutputFormatConfig": {
      "FileType": "{{ FileType }}",
      "PrefixConfig": {
       "PrefixType": "{{ PrefixType }}",
       "PrefixFormat": "{{ PrefixFormat }}",
       "PathPrefixHierarchy": [
        "{{ PathPrefixHierarchy[0] }}"
       ]
      },
      "AggregationConfig": {
       "AggregationType": "{{ AggregationType }}",
       "TargetFileSize": "{{ TargetFileSize }}"
      },
      "PreserveSourceDataTyping": "{{ PreserveSourceDataTyping }}"
     }
    },
    "Salesforce": {
     "Object": null,
     "ErrorHandlingConfig": null,
     "IdFieldNames": [
      "{{ IdFieldNames[0] }}"
     ],
     "WriteOperationType": "{{ WriteOperationType }}",
     "DataTransferApi": null
    },
    "Snowflake": {
     "Object": null,
     "IntermediateBucketName": null,
     "BucketPrefix": null,
     "ErrorHandlingConfig": null
    },
    "EventBridge": {
     "Object": null,
     "ErrorHandlingConfig": null
    },
    "Upsolver": {
     "BucketName": "{{ BucketName }}",
     "BucketPrefix": null,
     "S3OutputFormatConfig": {
      "FileType": null,
      "PrefixConfig": null,
      "AggregationConfig": null
     }
    },
    "LookoutMetrics": {
     "Object": null
    },
    "Marketo": {
     "Object": null,
     "ErrorHandlingConfig": null
    },
    "Zendesk": {
     "Object": null,
     "ErrorHandlingConfig": null,
     "IdFieldNames": [
      "{{ IdFieldNames[0] }}"
     ],
     "WriteOperationType": null
    },
    "CustomConnector": {
     "EntityName": null,
     "ErrorHandlingConfig": null,
     "WriteOperationType": null,
     "IdFieldNames": [
      "{{ IdFieldNames[0] }}"
     ],
     "CustomProperties": null
    },
    "SAPOData": {
     "ObjectPath": null,
     "ErrorHandlingConfig": null,
     "SuccessResponseHandlingConfig": {
      "BucketPrefix": null,
      "BucketName": null
     },
     "IdFieldNames": [
      "{{ IdFieldNames[0] }}"
     ],
     "WriteOperationType": null
    }
   }
  }
 ],
 "Tasks": [
  {
   "SourceFields": [
    "{{ SourceFields[0] }}"
   ],
   "ConnectorOperator": {
    "Amplitude": "{{ Amplitude }}",
    "Datadog": "{{ Datadog }}",
    "Dynatrace": "{{ Dynatrace }}",
    "GoogleAnalytics": "{{ GoogleAnalytics }}",
    "InforNexus": "{{ InforNexus }}",
    "Marketo": "{{ Marketo }}",
    "S3": "{{ S3 }}",
    "SAPOData": "{{ SAPOData }}",
    "Salesforce": "{{ Salesforce }}",
    "Pardot": "{{ Pardot }}",
    "ServiceNow": "{{ ServiceNow }}",
    "Singular": "{{ Singular }}",
    "Slack": "{{ Slack }}",
    "Trendmicro": "{{ Trendmicro }}",
    "Veeva": "{{ Veeva }}",
    "Zendesk": "{{ Zendesk }}",
    "CustomConnector": "{{ CustomConnector }}"
   },
   "DestinationField": "{{ DestinationField }}",
   "TaskType": "{{ TaskType }}",
   "TaskProperties": [
    {
     "Key": "{{ Key }}",
     "Value": "{{ Value }}"
    }
   ]
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.appflow.flows (
 FlowName,
 TriggerConfig,
 SourceFlowConfig,
 DestinationFlowConfigList,
 Tasks,
 region
)
SELECT 
{{ .FlowName }},
 {{ .TriggerConfig }},
 {{ .SourceFlowConfig }},
 {{ .DestinationFlowConfigList }},
 {{ .Tasks }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "FlowName": "{{ FlowName }}",
 "Description": "{{ Description }}",
 "KMSArn": "{{ KMSArn }}",
 "TriggerConfig": {
  "TriggerType": "{{ TriggerType }}",
  "TriggerProperties": {
   "ScheduleExpression": "{{ ScheduleExpression }}",
   "DataPullMode": "{{ DataPullMode }}",
   "ScheduleStartTime": null,
   "ScheduleEndTime": null,
   "FirstExecutionFrom": null,
   "TimeZone": "{{ TimeZone }}",
   "ScheduleOffset": null,
   "FlowErrorDeactivationThreshold": "{{ FlowErrorDeactivationThreshold }}"
  }
 },
 "FlowStatus": "{{ FlowStatus }}",
 "SourceFlowConfig": {
  "ConnectorType": "{{ ConnectorType }}",
  "ApiVersion": "{{ ApiVersion }}",
  "ConnectorProfileName": "{{ ConnectorProfileName }}",
  "SourceConnectorProperties": {
   "Amplitude": {
    "Object": "{{ Object }}"
   },
   "Datadog": {
    "Object": null
   },
   "Dynatrace": {
    "Object": null
   },
   "GoogleAnalytics": {
    "Object": null
   },
   "InforNexus": {
    "Object": null
   },
   "Marketo": {
    "Object": null
   },
   "S3": {
    "BucketName": "{{ BucketName }}",
    "BucketPrefix": "{{ BucketPrefix }}",
    "S3InputFormatConfig": {
     "S3InputFileType": "{{ S3InputFileType }}"
    }
   },
   "SAPOData": {
    "ObjectPath": null,
    "parallelismConfig": {
     "maxParallelism": "{{ maxParallelism }}"
    },
    "paginationConfig": {
     "maxPageSize": "{{ maxPageSize }}"
    }
   },
   "Salesforce": {
    "Object": null,
    "EnableDynamicFieldUpdate": "{{ EnableDynamicFieldUpdate }}",
    "IncludeDeletedRecords": "{{ IncludeDeletedRecords }}",
    "DataTransferApi": "{{ DataTransferApi }}"
   },
   "Pardot": {
    "Object": null
   },
   "ServiceNow": {
    "Object": null
   },
   "Singular": {
    "Object": null
   },
   "Slack": {
    "Object": null
   },
   "Trendmicro": {
    "Object": null
   },
   "Veeva": {
    "Object": null,
    "DocumentType": "{{ DocumentType }}",
    "IncludeSourceFiles": "{{ IncludeSourceFiles }}",
    "IncludeRenditions": "{{ IncludeRenditions }}",
    "IncludeAllVersions": "{{ IncludeAllVersions }}"
   },
   "Zendesk": {
    "Object": null
   },
   "CustomConnector": {
    "EntityName": "{{ EntityName }}",
    "CustomProperties": {},
    "DataTransferApi": {
     "Name": "{{ Name }}",
     "Type": "{{ Type }}"
    }
   }
  },
  "IncrementalPullConfig": {
   "DatetimeTypeFieldName": "{{ DatetimeTypeFieldName }}"
  }
 },
 "DestinationFlowConfigList": [
  {
   "ConnectorType": null,
   "ApiVersion": null,
   "ConnectorProfileName": null,
   "DestinationConnectorProperties": {
    "Redshift": {
     "Object": null,
     "IntermediateBucketName": null,
     "BucketPrefix": null,
     "ErrorHandlingConfig": {
      "FailOnFirstError": "{{ FailOnFirstError }}",
      "BucketPrefix": null,
      "BucketName": null
     }
    },
    "S3": {
     "BucketName": null,
     "BucketPrefix": null,
     "S3OutputFormatConfig": {
      "FileType": "{{ FileType }}",
      "PrefixConfig": {
       "PrefixType": "{{ PrefixType }}",
       "PrefixFormat": "{{ PrefixFormat }}",
       "PathPrefixHierarchy": [
        "{{ PathPrefixHierarchy[0] }}"
       ]
      },
      "AggregationConfig": {
       "AggregationType": "{{ AggregationType }}",
       "TargetFileSize": "{{ TargetFileSize }}"
      },
      "PreserveSourceDataTyping": "{{ PreserveSourceDataTyping }}"
     }
    },
    "Salesforce": {
     "Object": null,
     "ErrorHandlingConfig": null,
     "IdFieldNames": [
      "{{ IdFieldNames[0] }}"
     ],
     "WriteOperationType": "{{ WriteOperationType }}",
     "DataTransferApi": null
    },
    "Snowflake": {
     "Object": null,
     "IntermediateBucketName": null,
     "BucketPrefix": null,
     "ErrorHandlingConfig": null
    },
    "EventBridge": {
     "Object": null,
     "ErrorHandlingConfig": null
    },
    "Upsolver": {
     "BucketName": "{{ BucketName }}",
     "BucketPrefix": null,
     "S3OutputFormatConfig": {
      "FileType": null,
      "PrefixConfig": null,
      "AggregationConfig": null
     }
    },
    "LookoutMetrics": {
     "Object": null
    },
    "Marketo": {
     "Object": null,
     "ErrorHandlingConfig": null
    },
    "Zendesk": {
     "Object": null,
     "ErrorHandlingConfig": null,
     "IdFieldNames": [
      "{{ IdFieldNames[0] }}"
     ],
     "WriteOperationType": null
    },
    "CustomConnector": {
     "EntityName": null,
     "ErrorHandlingConfig": null,
     "WriteOperationType": null,
     "IdFieldNames": [
      "{{ IdFieldNames[0] }}"
     ],
     "CustomProperties": null
    },
    "SAPOData": {
     "ObjectPath": null,
     "ErrorHandlingConfig": null,
     "SuccessResponseHandlingConfig": {
      "BucketPrefix": null,
      "BucketName": null
     },
     "IdFieldNames": [
      "{{ IdFieldNames[0] }}"
     ],
     "WriteOperationType": null
    }
   }
  }
 ],
 "Tasks": [
  {
   "SourceFields": [
    "{{ SourceFields[0] }}"
   ],
   "ConnectorOperator": {
    "Amplitude": "{{ Amplitude }}",
    "Datadog": "{{ Datadog }}",
    "Dynatrace": "{{ Dynatrace }}",
    "GoogleAnalytics": "{{ GoogleAnalytics }}",
    "InforNexus": "{{ InforNexus }}",
    "Marketo": "{{ Marketo }}",
    "S3": "{{ S3 }}",
    "SAPOData": "{{ SAPOData }}",
    "Salesforce": "{{ Salesforce }}",
    "Pardot": "{{ Pardot }}",
    "ServiceNow": "{{ ServiceNow }}",
    "Singular": "{{ Singular }}",
    "Slack": "{{ Slack }}",
    "Trendmicro": "{{ Trendmicro }}",
    "Veeva": "{{ Veeva }}",
    "Zendesk": "{{ Zendesk }}",
    "CustomConnector": "{{ CustomConnector }}"
   },
   "DestinationField": "{{ DestinationField }}",
   "TaskType": "{{ TaskType }}",
   "TaskProperties": [
    {
     "Key": "{{ Key }}",
     "Value": "{{ Value }}"
    }
   ]
  }
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "MetadataCatalogConfig": {
  "GlueDataCatalog": {
   "RoleArn": "{{ RoleArn }}",
   "DatabaseName": "{{ DatabaseName }}",
   "TablePrefix": "{{ TablePrefix }}"
  }
 }
}
>>>
--all properties
INSERT INTO aws.appflow.flows (
 FlowName,
 Description,
 KMSArn,
 TriggerConfig,
 FlowStatus,
 SourceFlowConfig,
 DestinationFlowConfigList,
 Tasks,
 Tags,
 MetadataCatalogConfig,
 region
)
SELECT 
 {{ .FlowName }},
 {{ .Description }},
 {{ .KMSArn }},
 {{ .TriggerConfig }},
 {{ .FlowStatus }},
 {{ .SourceFlowConfig }},
 {{ .DestinationFlowConfigList }},
 {{ .Tasks }},
 {{ .Tags }},
 {{ .MetadataCatalogConfig }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.appflow.flows
WHERE data__Identifier = '<FlowName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>flows</code> resource, the following permissions are required:

### Create
```json
appflow:CreateFlow,
appflow:StartFlow,
appflow:TagResource,
appflow:ListTagsForResource,
appflow:UseConnectorProfile,
iam:PassRole,
s3:ListAllMyBuckets,
s3:GetBucketLocation,
s3:GetBucketPolicy,
kms:ListGrants,
kms:ListKeys,
kms:DescribeKey,
kms:ListAliases,
kms:CreateGrant,
secretsmanager:CreateSecret,
secretsmanager:PutResourcePolicy
```

### Delete
```json
appflow:DeleteFlow
```

### List
```json
appflow:ListFlows
```

