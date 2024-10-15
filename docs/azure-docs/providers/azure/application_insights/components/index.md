---
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
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

Creates, updates, deletes, gets or lists a <code>components</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.components" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_components', value: 'view', },
        { label: 'components', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="app_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="application__type" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_string" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_ip_masking" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_local_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource etag |
| <CopyableCode code="flow__type" /> | `text` | field from the `properties` object |
| <CopyableCode code="force_customer_storage_for_profiler" /> | `text` | field from the `properties` object |
| <CopyableCode code="hockey_app_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="hockey_app_token" /> | `text` | field from the `properties` object |
| <CopyableCode code="immediate_purge_data_on30_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="ingestion_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="instrumentation_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone. |
| <CopyableCode code="la_migration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="private_link_scoped_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access_for_ingestion" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access_for_query" /> | `text` | field from the `properties` object |
| <CopyableCode code="request__source" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="sampling_percentage" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
| <CopyableCode code="workspace_resource_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="etag" /> | `string` | Resource etag |
| <CopyableCode code="kind" /> | `string` | The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties that define an Application Insights component resource. |
| <CopyableCode code="tags" /> | `` | Resource tags |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Returns an Application Insights component. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all Application Insights components within a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of Application Insights components within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, data__kind" /> | Creates (or updates) an Application Insights component. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Deletes an Application Insights component. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, data__filters, data__table" /> | Purges data in an Application Insights component by a set of user-defined filters.

In order to manage system resources, purge requests are throttled at 50 requests per hour. You should batch the execution of purge requests by sending a single command whose predicate includes all user identities that require purging. Use the in operator to specify multiple identities. You should run the query prior to using for a purge request to verify that the results are expected.
Note: this operation is intended for Classic resources, for  workspace-based Application Insights resource please run purge operation (directly on the workspace)(https://docs.microsoft.com/en-us/rest/api/loganalytics/workspace-purge/purge) , scoped to specific resource id. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Updates an existing component's tags. To update other fields use the CreateOrUpdate method. |

## `SELECT` examples

Gets a list of all Application Insights components within a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_components', value: 'view', },
        { label: 'components', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
app_id,
application__type,
application_id,
connection_string,
creation_date,
disable_ip_masking,
disable_local_auth,
etag,
flow__type,
force_customer_storage_for_profiler,
hockey_app_id,
hockey_app_token,
immediate_purge_data_on30_days,
ingestion_mode,
instrumentation_key,
kind,
la_migration_date,
location,
private_link_scoped_resources,
provisioning_state,
public_network_access_for_ingestion,
public_network_access_for_query,
request__source,
resourceGroupName,
resourceName,
retention_in_days,
sampling_percentage,
subscriptionId,
tags,
tenant_id,
type,
workspace_resource_id
FROM azure.application_insights.vw_components
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
kind,
location,
properties,
tags,
type
FROM azure.application_insights.components
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>components</code> resource.

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
INSERT INTO azure.application_insights.components (
resourceGroupName,
resourceName,
subscriptionId,
data__kind,
kind,
etag,
properties,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ data__kind }}',
'{{ kind }}',
'{{ etag }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: etag
      value: string
    - name: properties
      value:
        - name: ApplicationId
          value: string
        - name: AppId
          value: string
        - name: Name
          value: string
        - name: Application_Type
          value: string
        - name: Flow_Type
          value: string
        - name: Request_Source
          value: string
        - name: InstrumentationKey
          value: string
        - name: CreationDate
          value: string
        - name: TenantId
          value: string
        - name: HockeyAppId
          value: string
        - name: HockeyAppToken
          value: string
        - name: provisioningState
          value: string
        - name: SamplingPercentage
          value: number
        - name: ConnectionString
          value: string
        - name: RetentionInDays
          value: integer
        - name: DisableIpMasking
          value: boolean
        - name: ImmediatePurgeDataOn30Days
          value: boolean
        - name: WorkspaceResourceId
          value: string
        - name: LaMigrationDate
          value: string
        - name: PrivateLinkScopedResources
          value:
            - - name: ResourceId
                value: string
              - name: ScopeId
                value: string
        - name: publicNetworkAccessForIngestion
          value: []
        - name: IngestionMode
          value: string
        - name: DisableLocalAuth
          value: boolean
        - name: ForceCustomerStorageForProfiler
          value: boolean
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>components</code> resource.

```sql
/*+ delete */
DELETE FROM azure.application_insights.components
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
