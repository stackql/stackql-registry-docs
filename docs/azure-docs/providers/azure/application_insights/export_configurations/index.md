---
title: export_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - export_configurations
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>export_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>export_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.export_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ApplicationName" /> | `string` | The name of the Application Insights component. |
| <CopyableCode code="ContainerName" /> | `string` | The name of the destination storage container. |
| <CopyableCode code="DestinationAccountId" /> | `string` | The name of destination account. |
| <CopyableCode code="DestinationStorageLocationId" /> | `string` | The destination account location ID. |
| <CopyableCode code="DestinationStorageSubscriptionId" /> | `string` | The destination storage account subscription ID. |
| <CopyableCode code="DestinationType" /> | `string` | The destination type. |
| <CopyableCode code="ExportId" /> | `string` | The unique ID of the export configuration inside an Application Insights component. It is auto generated when the Continuous Export configuration is created. |
| <CopyableCode code="ExportStatus" /> | `string` | This indicates current Continuous Export configuration status. The possible values are 'Preparing', 'Success', 'Failure'. |
| <CopyableCode code="InstrumentationKey" /> | `string` | The instrumentation key of the Application Insights component. |
| <CopyableCode code="IsUserEnabled" /> | `string` | This will be 'true' if the Continuous Export configuration is enabled, otherwise it will be 'false'. |
| <CopyableCode code="LastGapTime" /> | `string` | The last time the Continuous Export configuration started failing. |
| <CopyableCode code="LastSuccessTime" /> | `string` | The last time data was successfully delivered to the destination storage container for this Continuous Export configuration. |
| <CopyableCode code="LastUserUpdate" /> | `string` | Last time the Continuous Export configuration was updated. |
| <CopyableCode code="NotificationQueueEnabled" /> | `string` | Deprecated |
| <CopyableCode code="PermanentErrorReason" /> | `string` | This is the reason the Continuous Export configuration started failing. It can be 'AzureStorageNotFound' or 'AzureStorageAccessDenied'. |
| <CopyableCode code="RecordTypes" /> | `string` | This comma separated list of document types that will be exported. The possible values include 'Requests', 'Event', 'Exceptions', 'Metrics', 'PageViews', 'PageViewPerformance', 'Rdd', 'PerformanceCounters', 'Availability', 'Messages'. |
| <CopyableCode code="ResourceGroup" /> | `string` | The resource group of the Application Insights component. |
| <CopyableCode code="StorageName" /> | `string` | The name of the destination storage account. |
| <CopyableCode code="SubscriptionId" /> | `string` | The subscription of the Application Insights component. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="exportId, resourceGroupName, resourceName, subscriptionId" /> | Get the Continuous Export configuration for this export id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets a list of Continuous Export configuration of an Application Insights component. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create a Continuous Export configuration of an Application Insights component. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="exportId, resourceGroupName, resourceName, subscriptionId" /> | Delete a Continuous Export configuration of an Application Insights component. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="exportId, resourceGroupName, resourceName, subscriptionId" /> | Update the Continuous Export configuration for this export id. |

## `SELECT` examples

Gets a list of Continuous Export configuration of an Application Insights component.


```sql
SELECT
ApplicationName,
ContainerName,
DestinationAccountId,
DestinationStorageLocationId,
DestinationStorageSubscriptionId,
DestinationType,
ExportId,
ExportStatus,
InstrumentationKey,
IsUserEnabled,
LastGapTime,
LastSuccessTime,
LastUserUpdate,
NotificationQueueEnabled,
PermanentErrorReason,
RecordTypes,
ResourceGroup,
StorageName,
SubscriptionId
FROM azure.application_insights.export_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>export_configurations</code> resource.

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
INSERT INTO azure.application_insights.export_configurations (
resourceGroupName,
resourceName,
subscriptionId,
RecordTypes,
DestinationType,
DestinationAddress,
IsEnabled,
NotificationQueueEnabled,
NotificationQueueUri,
DestinationStorageSubscriptionId,
DestinationStorageLocationId,
DestinationAccountId
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ RecordTypes }}',
'{{ DestinationType }}',
'{{ DestinationAddress }}',
'{{ IsEnabled }}',
'{{ NotificationQueueEnabled }}',
'{{ NotificationQueueUri }}',
'{{ DestinationStorageSubscriptionId }}',
'{{ DestinationStorageLocationId }}',
'{{ DestinationAccountId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: RecordTypes
      value: string
    - name: DestinationType
      value: string
    - name: DestinationAddress
      value: string
    - name: IsEnabled
      value: string
    - name: NotificationQueueEnabled
      value: string
    - name: NotificationQueueUri
      value: string
    - name: DestinationStorageSubscriptionId
      value: string
    - name: DestinationStorageLocationId
      value: string
    - name: DestinationAccountId
      value: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>export_configurations</code> resource.

```sql
/*+ update */
REPLACE azure.application_insights.export_configurations
SET 
RecordTypes = '{{ RecordTypes }}',
DestinationType = '{{ DestinationType }}',
DestinationAddress = '{{ DestinationAddress }}',
IsEnabled = '{{ IsEnabled }}',
NotificationQueueEnabled = '{{ NotificationQueueEnabled }}',
NotificationQueueUri = '{{ NotificationQueueUri }}',
DestinationStorageSubscriptionId = '{{ DestinationStorageSubscriptionId }}',
DestinationStorageLocationId = '{{ DestinationStorageLocationId }}',
DestinationAccountId = '{{ DestinationAccountId }}'
WHERE 
exportId = '{{ exportId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>export_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.application_insights.export_configurations
WHERE exportId = '{{ exportId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
