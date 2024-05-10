---
title: configs
hide_title: false
hide_table_of_contents: false
keywords:
  - configs
  - groundstation
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


Used to retrieve a list of <code>configs</code> in a region or to create or delete a <code>configs</code> resource, use <code>config</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Ground Station config resource type for CloudFormation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.groundstation.configs" /></td></tr>
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
FROM aws.groundstation.configs
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
 "Name": "{{ Name }}",
 "ConfigData": {
  "AntennaDownlinkConfig": {
   "SpectrumConfig": {
    "CenterFrequency": {
     "Value": null,
     "Units": "{{ Units }}"
    },
    "Bandwidth": {
     "Value": null,
     "Units": "{{ Units }}"
    },
    "Polarization": "{{ Polarization }}"
   }
  },
  "TrackingConfig": {
   "Autotrack": "{{ Autotrack }}"
  },
  "DataflowEndpointConfig": {
   "DataflowEndpointName": "{{ DataflowEndpointName }}",
   "DataflowEndpointRegion": "{{ DataflowEndpointRegion }}"
  },
  "AntennaDownlinkDemodDecodeConfig": {
   "SpectrumConfig": null,
   "DemodulationConfig": {
    "UnvalidatedJSON": "{{ UnvalidatedJSON }}"
   },
   "DecodeConfig": {
    "UnvalidatedJSON": null
   }
  },
  "AntennaUplinkConfig": {
   "SpectrumConfig": {
    "CenterFrequency": null,
    "Polarization": null
   },
   "TargetEirp": {
    "Value": null,
    "Units": "{{ Units }}"
   },
   "TransmitDisabled": "{{ TransmitDisabled }}"
  },
  "UplinkEchoConfig": {
   "Enabled": "{{ Enabled }}",
   "AntennaUplinkConfigArn": "{{ AntennaUplinkConfigArn }}"
  },
  "S3RecordingConfig": {
   "BucketArn": "{{ BucketArn }}",
   "RoleArn": "{{ RoleArn }}",
   "Prefix": "{{ Prefix }}"
  }
 }
}
>>>
--required properties only
INSERT INTO aws.groundstation.configs (
 Name,
 ConfigData,
 region
)
SELECT 
{{ .Name }},
 {{ .ConfigData }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "ConfigData": {
  "AntennaDownlinkConfig": {
   "SpectrumConfig": {
    "CenterFrequency": {
     "Value": null,
     "Units": "{{ Units }}"
    },
    "Bandwidth": {
     "Value": null,
     "Units": "{{ Units }}"
    },
    "Polarization": "{{ Polarization }}"
   }
  },
  "TrackingConfig": {
   "Autotrack": "{{ Autotrack }}"
  },
  "DataflowEndpointConfig": {
   "DataflowEndpointName": "{{ DataflowEndpointName }}",
   "DataflowEndpointRegion": "{{ DataflowEndpointRegion }}"
  },
  "AntennaDownlinkDemodDecodeConfig": {
   "SpectrumConfig": null,
   "DemodulationConfig": {
    "UnvalidatedJSON": "{{ UnvalidatedJSON }}"
   },
   "DecodeConfig": {
    "UnvalidatedJSON": null
   }
  },
  "AntennaUplinkConfig": {
   "SpectrumConfig": {
    "CenterFrequency": null,
    "Polarization": null
   },
   "TargetEirp": {
    "Value": null,
    "Units": "{{ Units }}"
   },
   "TransmitDisabled": "{{ TransmitDisabled }}"
  },
  "UplinkEchoConfig": {
   "Enabled": "{{ Enabled }}",
   "AntennaUplinkConfigArn": "{{ AntennaUplinkConfigArn }}"
  },
  "S3RecordingConfig": {
   "BucketArn": "{{ BucketArn }}",
   "RoleArn": "{{ RoleArn }}",
   "Prefix": "{{ Prefix }}"
  }
 }
}
>>>
--all properties
INSERT INTO aws.groundstation.configs (
 Name,
 Tags,
 ConfigData,
 region
)
SELECT 
 {{ .Name }},
 {{ .Tags }},
 {{ .ConfigData }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.groundstation.configs
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configs</code> resource, the following permissions are required:

### Create
```json
groundstation:CreateConfig,
groundstation:TagResource,
iam:PassRole
```

### Delete
```json
groundstation:DeleteConfig
```

### List
```json
groundstation:ListConfigs
```

