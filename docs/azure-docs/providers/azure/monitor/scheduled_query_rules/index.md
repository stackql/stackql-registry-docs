---
title: scheduled_query_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_query_rules
  - monitor
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>scheduled_query_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_query_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.scheduled_query_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scheduled_query_rules', value: 'view', },
        { label: 'scheduled_query_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_mitigate" /> | `text` | field from the `properties` object |
| <CopyableCode code="check_workspace_alerts_storage_configured" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_with_api_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="criteria" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| <CopyableCode code="evaluation_frequency" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="is_legacy_log_analytics_rule" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_workspace_alerts_storage_configured" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Indicates the type of scheduled query rule. The default is LogAlert. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mute_actions_duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="override_query_time_range" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rule_resolve_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="skip_query_validation" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="target_resource_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="window_size" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="etag" /> | `string` | The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | Indicates the type of scheduled query rule. The default is LogAlert. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | scheduled query rule Definition |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId" /> | Retrieve an scheduled query rule definition. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieve scheduled query rule definitions in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieve a scheduled query rule definitions in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId, data__location, data__properties" /> | Creates or updates a scheduled query rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId" /> | Deletes a scheduled query rule. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId" /> | Update a scheduled query rule. |
| <CopyableCode code="reconcile_nsp" /> | `EXEC` | <CopyableCode code="networkSecurityPerimeterConfigurationName, resourceGroupName, ruleName, subscriptionId" /> | Reconcile network security perimeter configuration for ScheduledQueryRule resource. |

## `SELECT` examples

Retrieve a scheduled query rule definitions in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scheduled_query_rules', value: 'view', },
        { label: 'scheduled_query_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
actions,
auto_mitigate,
check_workspace_alerts_storage_configured,
created_with_api_version,
criteria,
display_name,
enabled,
etag,
evaluation_frequency,
identity,
is_legacy_log_analytics_rule,
is_workspace_alerts_storage_configured,
kind,
location,
mute_actions_duration,
override_query_time_range,
resourceGroupName,
ruleName,
rule_resolve_configuration,
scopes,
severity,
skip_query_validation,
subscriptionId,
system_data,
tags,
target_resource_types,
type,
window_size
FROM azure.monitor.vw_scheduled_query_rules
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
identity,
kind,
location,
properties,
systemData,
tags,
type
FROM azure.monitor.scheduled_query_rules
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scheduled_query_rules</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.monitor.scheduled_query_rules (
resourceGroupName,
ruleName,
subscriptionId,
data__location,
data__properties,
identity,
tags,
location,
kind,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ ruleName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ identity }}',
'{{ tags }}',
'{{ location }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: tags
      value: object
    - name: location
      value: string
    - name: kind
      value: string
    - name: etag
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: createdWithApiVersion
          value: string
        - name: isLegacyLogAnalyticsRule
          value: boolean
        - name: description
          value: string
        - name: displayName
          value: string
        - name: severity
          value: integer
        - name: enabled
          value: boolean
        - name: scopes
          value:
            - string
        - name: evaluationFrequency
          value: string
        - name: windowSize
          value: string
        - name: overrideQueryTimeRange
          value: string
        - name: targetResourceTypes
          value:
            - string
        - name: criteria
          value:
            - name: allOf
              value:
                - - name: query
                    value: string
                  - name: timeAggregation
                    value: string
                  - name: metricMeasureColumn
                    value: string
                  - name: resourceIdColumn
                    value: string
                  - name: dimensions
                    value:
                      - - name: name
                          value: string
                        - name: operator
                          value: string
                        - name: values
                          value:
                            - string
                  - name: operator
                    value: string
                  - name: threshold
                    value: number
                  - name: failingPeriods
                    value:
                      - name: numberOfEvaluationPeriods
                        value: integer
                      - name: minFailingPeriodsToAlert
                        value: integer
                  - name: metricName
                    value: string
        - name: muteActionsDuration
          value: string
        - name: actions
          value:
            - name: actionGroups
              value:
                - string
            - name: customProperties
              value: object
            - name: actionProperties
              value: object
        - name: isWorkspaceAlertsStorageConfigured
          value: boolean
        - name: checkWorkspaceAlertsStorageConfigured
          value: boolean
        - name: skipQueryValidation
          value: boolean
        - name: autoMitigate
          value: boolean
        - name: ruleResolveConfiguration
          value:
            - name: autoResolved
              value: boolean
            - name: timeToResolve
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>scheduled_query_rules</code> resource.

```sql
/*+ update */
UPDATE azure.monitor.scheduled_query_rules
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND ruleName = '{{ ruleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>scheduled_query_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.monitor.scheduled_query_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND ruleName = '{{ ruleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
