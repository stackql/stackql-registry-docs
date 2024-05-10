---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - applicationinsights
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


Used to retrieve a list of <code>applications</code> in a region or to create or delete a <code>applications</code> resource, use <code>application</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ApplicationInsights::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.applicationinsights.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The ARN of the ApplicationInsights application.</td></tr>
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
application_arn
FROM aws.applicationinsights.applications
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
 "ResourceGroupName": "{{ ResourceGroupName }}"
}
>>>
--required properties only
INSERT INTO aws.applicationinsights.applications (
 ResourceGroupName,
 region
)
SELECT 
{{ ResourceGroupName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ResourceGroupName": "{{ ResourceGroupName }}",
 "CWEMonitorEnabled": "{{ CWEMonitorEnabled }}",
 "OpsCenterEnabled": "{{ OpsCenterEnabled }}",
 "OpsItemSNSTopicArn": "{{ OpsItemSNSTopicArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "CustomComponents": [
  {
   "ComponentName": "{{ ComponentName }}",
   "ResourceList": [
    "{{ ResourceList[0] }}"
   ]
  }
 ],
 "LogPatternSets": [
  {
   "PatternSetName": "{{ PatternSetName }}",
   "LogPatterns": [
    {
     "PatternName": "{{ PatternName }}",
     "Pattern": "{{ Pattern }}",
     "Rank": "{{ Rank }}"
    }
   ]
  }
 ],
 "AutoConfigurationEnabled": "{{ AutoConfigurationEnabled }}",
 "ComponentMonitoringSettings": [
  {
   "ComponentName": "{{ ComponentName }}",
   "ComponentARN": "{{ ComponentARN }}",
   "Tier": "{{ Tier }}",
   "ComponentConfigurationMode": "{{ ComponentConfigurationMode }}",
   "DefaultOverwriteComponentConfiguration": {
    "ConfigurationDetails": {
     "AlarmMetrics": [
      {
       "AlarmMetricName": "{{ AlarmMetricName }}"
      }
     ],
     "Logs": [
      {
       "LogGroupName": "{{ LogGroupName }}",
       "LogPath": "{{ LogPath }}",
       "LogType": "{{ LogType }}",
       "Encoding": "{{ Encoding }}",
       "PatternSet": "{{ PatternSet }}"
      }
     ],
     "WindowsEvents": [
      {
       "LogGroupName": "{{ LogGroupName }}",
       "EventName": "{{ EventName }}",
       "EventLevels": [
        "{{ EventLevels[0] }}"
       ],
       "PatternSet": "{{ PatternSet }}"
      }
     ],
     "Processes": [
      {
       "ProcessName": "{{ ProcessName }}",
       "AlarmMetrics": [
        null
       ]
      }
     ],
     "Alarms": [
      {
       "AlarmName": "{{ AlarmName }}",
       "Severity": "{{ Severity }}"
      }
     ],
     "JMXPrometheusExporter": {
      "JMXURL": "{{ JMXURL }}",
      "HostPort": "{{ HostPort }}",
      "PrometheusPort": "{{ PrometheusPort }}"
     },
     "HANAPrometheusExporter": {
      "HANASID": "{{ HANASID }}",
      "HANAPort": "{{ HANAPort }}",
      "HANASecretName": "{{ HANASecretName }}",
      "AgreeToInstallHANADBClient": "{{ AgreeToInstallHANADBClient }}",
      "PrometheusPort": "{{ PrometheusPort }}"
     },
     "HAClusterPrometheusExporter": {
      "PrometheusPort": "{{ PrometheusPort }}"
     },
     "NetWeaverPrometheusExporter": {
      "SAPSID": "{{ SAPSID }}",
      "InstanceNumbers": [
       "{{ InstanceNumbers[0] }}"
      ],
      "PrometheusPort": "{{ PrometheusPort }}"
     },
     "SQLServerPrometheusExporter": {
      "PrometheusPort": "{{ PrometheusPort }}",
      "SQLSecretName": "{{ SQLSecretName }}"
     }
    },
    "SubComponentTypeConfigurations": [
     {
      "SubComponentType": "{{ SubComponentType }}",
      "SubComponentConfigurationDetails": {
       "AlarmMetrics": [
        null
       ],
       "Logs": [
        null
       ],
       "WindowsEvents": [
        null
       ],
       "Processes": [
        null
       ]
      }
     }
    ]
   },
   "CustomComponentConfiguration": null
  }
 ],
 "GroupingType": "{{ GroupingType }}",
 "AttachMissingPermission": "{{ AttachMissingPermission }}"
}
>>>
--all properties
INSERT INTO aws.applicationinsights.applications (
 ResourceGroupName,
 CWEMonitorEnabled,
 OpsCenterEnabled,
 OpsItemSNSTopicArn,
 Tags,
 CustomComponents,
 LogPatternSets,
 AutoConfigurationEnabled,
 ComponentMonitoringSettings,
 GroupingType,
 AttachMissingPermission,
 region
)
SELECT 
 {{ ResourceGroupName }},
 {{ CWEMonitorEnabled }},
 {{ OpsCenterEnabled }},
 {{ OpsItemSNSTopicArn }},
 {{ Tags }},
 {{ CustomComponents }},
 {{ LogPatternSets }},
 {{ AutoConfigurationEnabled }},
 {{ ComponentMonitoringSettings }},
 {{ GroupingType }},
 {{ AttachMissingPermission }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.applicationinsights.applications
WHERE data__Identifier = '<ApplicationARN>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
*
```

### Delete
```json
*
```

### List
```json
*
```

