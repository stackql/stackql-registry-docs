---
title: deleted_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_accounts
  - cognitive_services
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

Creates, updates, deletes, gets or lists a <code>deleted_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deleted_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.deleted_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deleted_accounts', value: 'view', },
        { label: 'deleted_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="abuse_penalty" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="allowed_fqdn_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="aml_workspace" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="call_rate_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="commitment_plan_associations" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_sub_domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="date_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="deletion_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_local_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="dynamic_throttling_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource Etag. |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="internal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_migrated" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The kind (type) of cognitive service account. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_token" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_acls" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="quota_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="rai_monitor_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore" /> | `text` | field from the `properties` object |
| <CopyableCode code="restrict_outbound_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_purge_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="sku_change_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="user_owned_storage" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | The kind (type) of cognitive service account. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of Cognitive Services account. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, location, resourceGroupName, subscriptionId" /> | Returns a Cognitive Services account specified by the parameters. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns all the resources of a particular type belonging to a subscription. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="accountName, location, resourceGroupName, subscriptionId" /> | Deletes a Cognitive Services account from the resource group.  |

## `SELECT` examples

Returns all the resources of a particular type belonging to a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deleted_accounts', value: 'view', },
        { label: 'deleted_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
abuse_penalty,
accountName,
allowed_fqdn_list,
aml_workspace,
api_properties,
call_rate_limit,
capabilities,
commitment_plan_associations,
custom_sub_domain_name,
date_created,
deletion_date,
disable_local_auth,
dynamic_throttling_enabled,
encryption,
endpoint,
endpoints,
etag,
identity,
internal_id,
is_migrated,
kind,
location,
locations,
migration_token,
network_acls,
private_endpoint_connections,
provisioning_state,
public_network_access,
quota_limit,
rai_monitor_config,
resourceGroupName,
restore,
restrict_outbound_network_access,
scheduled_purge_date,
sku,
sku_change_info,
subscriptionId,
system_data,
tags,
user_owned_storage
FROM azure.cognitive_services.vw_deleted_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
identity,
kind,
location,
properties,
sku,
systemData,
tags
FROM azure.cognitive_services.deleted_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

