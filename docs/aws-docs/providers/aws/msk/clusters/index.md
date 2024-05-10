---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - msk
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


Used to retrieve a list of <code>clusters</code> in a region or to create or delete a <code>clusters</code> resource, use <code>cluster</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::Cluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
arn
FROM aws.msk.clusters
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
 "BrokerNodeGroupInfo": {
  "StorageInfo": {
   "EBSStorageInfo": {
    "VolumeSize": "{{ VolumeSize }}",
    "ProvisionedThroughput": {
     "Enabled": "{{ Enabled }}",
     "VolumeThroughput": "{{ VolumeThroughput }}"
    }
   }
  },
  "ConnectivityInfo": {
   "PublicAccess": {
    "Type": "{{ Type }}"
   },
   "VpcConnectivity": {
    "ClientAuthentication": {
     "Tls": {
      "Enabled": "{{ Enabled }}"
     },
     "Sasl": {
      "Scram": {
       "Enabled": "{{ Enabled }}"
      },
      "Iam": {
       "Enabled": "{{ Enabled }}"
      }
     }
    }
   }
  },
  "SecurityGroups": [
   "{{ SecurityGroups[0] }}"
  ],
  "BrokerAZDistribution": "{{ BrokerAZDistribution }}",
  "ClientSubnets": [
   "{{ ClientSubnets[0] }}"
  ],
  "InstanceType": "{{ InstanceType }}"
 },
 "KafkaVersion": "{{ KafkaVersion }}",
 "NumberOfBrokerNodes": "{{ NumberOfBrokerNodes }}",
 "ClusterName": "{{ ClusterName }}"
}
>>>
--required properties only
INSERT INTO aws.msk.clusters (
 BrokerNodeGroupInfo,
 KafkaVersion,
 NumberOfBrokerNodes,
 ClusterName,
 region
)
SELECT 
{{ .BrokerNodeGroupInfo }},
 {{ .KafkaVersion }},
 {{ .NumberOfBrokerNodes }},
 {{ .ClusterName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "BrokerNodeGroupInfo": {
  "StorageInfo": {
   "EBSStorageInfo": {
    "VolumeSize": "{{ VolumeSize }}",
    "ProvisionedThroughput": {
     "Enabled": "{{ Enabled }}",
     "VolumeThroughput": "{{ VolumeThroughput }}"
    }
   }
  },
  "ConnectivityInfo": {
   "PublicAccess": {
    "Type": "{{ Type }}"
   },
   "VpcConnectivity": {
    "ClientAuthentication": {
     "Tls": {
      "Enabled": "{{ Enabled }}"
     },
     "Sasl": {
      "Scram": {
       "Enabled": "{{ Enabled }}"
      },
      "Iam": {
       "Enabled": "{{ Enabled }}"
      }
     }
    }
   }
  },
  "SecurityGroups": [
   "{{ SecurityGroups[0] }}"
  ],
  "BrokerAZDistribution": "{{ BrokerAZDistribution }}",
  "ClientSubnets": [
   "{{ ClientSubnets[0] }}"
  ],
  "InstanceType": "{{ InstanceType }}"
 },
 "EnhancedMonitoring": "{{ EnhancedMonitoring }}",
 "KafkaVersion": "{{ KafkaVersion }}",
 "NumberOfBrokerNodes": "{{ NumberOfBrokerNodes }}",
 "EncryptionInfo": {
  "EncryptionAtRest": {
   "DataVolumeKMSKeyId": "{{ DataVolumeKMSKeyId }}"
  },
  "EncryptionInTransit": {
   "InCluster": "{{ InCluster }}",
   "ClientBroker": "{{ ClientBroker }}"
  }
 },
 "OpenMonitoring": {
  "Prometheus": {
   "JmxExporter": {
    "EnabledInBroker": "{{ EnabledInBroker }}"
   },
   "NodeExporter": {
    "EnabledInBroker": "{{ EnabledInBroker }}"
   }
  }
 },
 "ClusterName": "{{ ClusterName }}",
 "CurrentVersion": "{{ CurrentVersion }}",
 "ClientAuthentication": {
  "Sasl": {
   "Iam": {
    "Enabled": "{{ Enabled }}"
   }
  }
 },
 "LoggingInfo": {
  "BrokerLogs": {
   "S3": {
    "Enabled": "{{ Enabled }}",
    "Prefix": "{{ Prefix }}",
    "Bucket": "{{ Bucket }}"
   },
   "CloudWatchLogs": {
    "LogGroup": "{{ LogGroup }}",
    "Enabled": "{{ Enabled }}"
   },
   "Firehose": {
    "Enabled": "{{ Enabled }}",
    "DeliveryStream": "{{ DeliveryStream }}"
   }
  }
 },
 "Tags": {},
 "ConfigurationInfo": {
  "Revision": "{{ Revision }}",
  "Arn": "{{ Arn }}"
 },
 "StorageMode": "{{ StorageMode }}"
}
>>>
--all properties
INSERT INTO aws.msk.clusters (
 BrokerNodeGroupInfo,
 EnhancedMonitoring,
 KafkaVersion,
 NumberOfBrokerNodes,
 EncryptionInfo,
 OpenMonitoring,
 ClusterName,
 CurrentVersion,
 ClientAuthentication,
 LoggingInfo,
 Tags,
 ConfigurationInfo,
 StorageMode,
 region
)
SELECT 
 {{ .BrokerNodeGroupInfo }},
 {{ .EnhancedMonitoring }},
 {{ .KafkaVersion }},
 {{ .NumberOfBrokerNodes }},
 {{ .EncryptionInfo }},
 {{ .OpenMonitoring }},
 {{ .ClusterName }},
 {{ .CurrentVersion }},
 {{ .ClientAuthentication }},
 {{ .LoggingInfo }},
 {{ .Tags }},
 {{ .ConfigurationInfo }},
 {{ .StorageMode }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.msk.clusters
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>clusters</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
iam:AttachRolePolicy,
iam:CreateServiceLinkedRole,
iam:PutRolePolicy,
kms:CreateGrant,
kms:DescribeKey,
kafka:CreateCluster,
kafka:DescribeCluster,
kafka:TagResource,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
firehose:TagDeliveryStream,
acm-pca:GetCertificateAuthorityCertificate
```

### Delete
```json
kafka:DeleteCluster,
kafka:DescribeCluster
```

### List
```json
kafka:ListClusters
```

