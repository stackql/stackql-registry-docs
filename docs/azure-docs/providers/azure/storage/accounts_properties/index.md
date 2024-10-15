---
title: accounts_properties
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_properties
  - storage
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

Creates, updates, deletes, gets or lists a <code>accounts_properties</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts_properties</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.accounts_properties" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_accounts_properties', value: 'view', },
        { label: 'accounts_properties', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="access_tier" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_migration_in_progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_blob_public_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_cross_tenant_replication" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_shared_key_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="allowed_copy_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_files_identity_based_authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="blob_restore_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_domain" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_to_oauth_authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_endpoint_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_extended_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="failover_in_progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="geo_replication_stats" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="immutable_storage_with_versioning" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_hns_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_local_user_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_nfs_v3_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_sftp_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_sku_conversion_blocked" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Gets the Kind. |
| <CopyableCode code="large_file_shares_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_geo_failover_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="minimum_tls_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_acls" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_preference" /> | `text` | field from the `properties` object |
| <CopyableCode code="sas_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="status_of_primary" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_of_secondary" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_sku_conversion_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supports_https_traffic_only" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | Gets the Kind. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the storage account. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Returns the properties for the specified storage account including but not limited to name, SKU name, location, and account status. The ListKeys operation should be used to retrieve storage keys. |

## `SELECT` examples

Returns the properties for the specified storage account including but not limited to name, SKU name, location, and account status. The ListKeys operation should be used to retrieve storage keys.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_accounts_properties', value: 'view', },
        { label: 'accounts_properties', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
access_tier,
accountName,
account_migration_in_progress,
allow_blob_public_access,
allow_cross_tenant_replication,
allow_shared_key_access,
allowed_copy_scope,
azure_files_identity_based_authentication,
blob_restore_status,
creation_time,
custom_domain,
default_to_oauth_authentication,
dns_endpoint_type,
enable_extended_groups,
encryption,
extended_location,
failover_in_progress,
geo_replication_stats,
identity,
immutable_storage_with_versioning,
is_hns_enabled,
is_local_user_enabled,
is_nfs_v3_enabled,
is_sftp_enabled,
is_sku_conversion_blocked,
key_creation_time,
key_policy,
kind,
large_file_shares_state,
last_geo_failover_time,
location,
minimum_tls_version,
network_acls,
primary_endpoints,
primary_location,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
routing_preference,
sas_policy,
secondary_endpoints,
secondary_location,
sku,
status_of_primary,
status_of_secondary,
storage_account_sku_conversion_status,
subscriptionId,
supports_https_traffic_only,
tags
FROM azure.storage.vw_accounts_properties
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
identity,
kind,
location,
properties,
sku,
tags
FROM azure.storage.accounts_properties
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

