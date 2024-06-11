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

Creates, updates, deletes or gets an <code>application</code> resource or lists <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ApplicationInsights::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.applicationinsights.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_group_name" /></td><td><code>string</code></td><td>The name of the resource group.</td></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The ARN of the ApplicationInsights application.</td></tr>
<tr><td><CopyableCode code="cwe_monitor_enabled" /></td><td><code>boolean</code></td><td>Indicates whether Application Insights can listen to CloudWatch events for the application resources.</td></tr>
<tr><td><CopyableCode code="ops_center_enabled" /></td><td><code>boolean</code></td><td>When set to true, creates opsItems for any problems detected on an application.</td></tr>
<tr><td><CopyableCode code="ops_item_sns_topic_arn" /></td><td><code>string</code></td><td>The SNS topic provided to Application Insights that is associated to the created opsItem.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags of Application Insights application.</td></tr>
<tr><td><CopyableCode code="custom_components" /></td><td><code>array</code></td><td>The custom grouped components.</td></tr>
<tr><td><CopyableCode code="log_pattern_sets" /></td><td><code>array</code></td><td>The log pattern sets.</td></tr>
<tr><td><CopyableCode code="auto_configuration_enabled" /></td><td><code>boolean</code></td><td>If set to true, application will be configured with recommended monitoring configuration.</td></tr>
<tr><td><CopyableCode code="component_monitoring_settings" /></td><td><code>array</code></td><td>The monitoring settings of the components.</td></tr>
<tr><td><CopyableCode code="grouping_type" /></td><td><code>string</code></td><td>The grouping type of the application</td></tr>
<tr><td><CopyableCode code="attach_missing_permission" /></td><td><code>boolean</code></td><td>If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing</td></tr>
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
    <td><CopyableCode code="ResourceGroupName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>applications</code> in a region.
```sql
SELECT
region,
application_arn
FROM aws.applicationinsights.applications
WHERE region = 'us-east-1';
```
Gets all properties from an <code>application</code>.
```sql
SELECT
region,
resource_group_name,
application_arn,
cwe_monitor_enabled,
ops_center_enabled,
ops_item_sns_topic_arn,
tags,
custom_components,
log_pattern_sets,
auto_configuration_enabled,
component_monitoring_settings,
grouping_type,
attach_missing_permission
FROM aws.applicationinsights.applications
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationARN>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.applicationinsights.applications (
 ResourceGroupName,
 region
)
SELECT 
'{{ ResourceGroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ ResourceGroupName }}',
 '{{ CWEMonitorEnabled }}',
 '{{ OpsCenterEnabled }}',
 '{{ OpsItemSNSTopicArn }}',
 '{{ Tags }}',
 '{{ CustomComponents }}',
 '{{ LogPatternSets }}',
 '{{ AutoConfigurationEnabled }}',
 '{{ ComponentMonitoringSettings }}',
 '{{ GroupingType }}',
 '{{ AttachMissingPermission }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: application
    props:
      - name: ResourceGroupName
        value: '{{ ResourceGroupName }}'
      - name: CWEMonitorEnabled
        value: '{{ CWEMonitorEnabled }}'
      - name: OpsCenterEnabled
        value: '{{ OpsCenterEnabled }}'
      - name: OpsItemSNSTopicArn
        value: '{{ OpsItemSNSTopicArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: CustomComponents
        value:
          - ComponentName: '{{ ComponentName }}'
            ResourceList:
              - '{{ ResourceList[0] }}'
      - name: LogPatternSets
        value:
          - PatternSetName: '{{ PatternSetName }}'
            LogPatterns:
              - PatternName: '{{ PatternName }}'
                Pattern: '{{ Pattern }}'
                Rank: '{{ Rank }}'
      - name: AutoConfigurationEnabled
        value: '{{ AutoConfigurationEnabled }}'
      - name: ComponentMonitoringSettings
        value:
          - ComponentName: '{{ ComponentName }}'
            ComponentARN: '{{ ComponentARN }}'
            Tier: '{{ Tier }}'
            ComponentConfigurationMode: '{{ ComponentConfigurationMode }}'
            DefaultOverwriteComponentConfiguration:
              ConfigurationDetails:
                AlarmMetrics:
                  - AlarmMetricName: '{{ AlarmMetricName }}'
                Logs:
                  - LogGroupName: '{{ LogGroupName }}'
                    LogPath: '{{ LogPath }}'
                    LogType: '{{ LogType }}'
                    Encoding: '{{ Encoding }}'
                    PatternSet: '{{ PatternSet }}'
                WindowsEvents:
                  - LogGroupName: '{{ LogGroupName }}'
                    EventName: '{{ EventName }}'
                    EventLevels:
                      - '{{ EventLevels[0] }}'
                    PatternSet: '{{ PatternSet }}'
                Processes:
                  - ProcessName: '{{ ProcessName }}'
                    AlarmMetrics:
                      - null
                Alarms:
                  - AlarmName: '{{ AlarmName }}'
                    Severity: '{{ Severity }}'
                JMXPrometheusExporter:
                  JMXURL: '{{ JMXURL }}'
                  HostPort: '{{ HostPort }}'
                  PrometheusPort: '{{ PrometheusPort }}'
                HANAPrometheusExporter:
                  HANASID: '{{ HANASID }}'
                  HANAPort: '{{ HANAPort }}'
                  HANASecretName: '{{ HANASecretName }}'
                  AgreeToInstallHANADBClient: '{{ AgreeToInstallHANADBClient }}'
                  PrometheusPort: '{{ PrometheusPort }}'
                HAClusterPrometheusExporter:
                  PrometheusPort: '{{ PrometheusPort }}'
                NetWeaverPrometheusExporter:
                  SAPSID: '{{ SAPSID }}'
                  InstanceNumbers:
                    - '{{ InstanceNumbers[0] }}'
                  PrometheusPort: '{{ PrometheusPort }}'
                SQLServerPrometheusExporter:
                  PrometheusPort: '{{ PrometheusPort }}'
                  SQLSecretName: '{{ SQLSecretName }}'
              SubComponentTypeConfigurations:
                - SubComponentType: '{{ SubComponentType }}'
                  SubComponentConfigurationDetails:
                    AlarmMetrics:
                      - null
                    Logs:
                      - null
                    WindowsEvents:
                      - null
                    Processes:
                      - null
            CustomComponentConfiguration: null
      - name: GroupingType
        value: '{{ GroupingType }}'
      - name: AttachMissingPermission
        value: '{{ AttachMissingPermission }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
*
```

### Update
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

