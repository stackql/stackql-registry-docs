---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - data_lake_analytics
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

Creates, updates, deletes, gets or lists a <code>accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_lake_analytics.accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_accounts', value: 'view', },
        { label: 'accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_tier" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_lake_store_accounts" /> | `text` | field from the `properties` object |
| <CopyableCode code="debug_data_access_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_data_lake_store_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_data_lake_store_account_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewall_allow_azure_ips" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewall_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewall_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="hive_metastores" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="max_active_job_count_per_user" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_degree_of_parallelism" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_degree_of_parallelism_per_job" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_job_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_job_running_time_in_min" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_queued_job_count_per_user" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_priority_per_job" /> | `text` | field from the `properties` object |
| <CopyableCode code="new_tier" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_data_lake_store_accounts" /> | `text` | field from the `properties` object |
| <CopyableCode code="query_store_retention" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_accounts" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_max_degree_of_parallelism" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_max_job_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | The resource type. |
| <CopyableCode code="virtual_network_rules" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The account specific properties that are associated with an underlying Data Lake Analytics account. Returned only when retrieving a specific account. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets details of the specified Data Lake Analytics account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the first page of Data Lake Analytics accounts, if any, within the current subscription. This includes a link to the next page, if any. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets the first page of Data Lake Analytics accounts, if any, within a specific resource group. This includes a link to the next page, if any. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Creates the specified Data Lake Analytics account. This supplies the user with computation services for Data Lake Analytics workloads. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Begins the delete process for the Data Lake Analytics account object specified by the account name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Updates the Data Lake Analytics account object specified by the accountName with the contents of the account object. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__type" /> | Checks whether the specified account name is available or taken. |

## `SELECT` examples

Gets the first page of Data Lake Analytics accounts, if any, within the current subscription. This includes a link to the next page, if any.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_accounts', value: 'view', },
        { label: 'accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
account_id,
compute_policies,
creation_time,
current_tier,
data_lake_store_accounts,
debug_data_access_level,
default_data_lake_store_account,
default_data_lake_store_account_type,
endpoint,
firewall_allow_azure_ips,
firewall_rules,
firewall_state,
hive_metastores,
last_modified_time,
location,
max_active_job_count_per_user,
max_degree_of_parallelism,
max_degree_of_parallelism_per_job,
max_job_count,
max_job_running_time_in_min,
max_queued_job_count_per_user,
min_priority_per_job,
new_tier,
provisioning_state,
public_data_lake_store_accounts,
query_store_retention,
resourceGroupName,
state,
storage_accounts,
subscriptionId,
system_max_degree_of_parallelism,
system_max_job_count,
tags,
type,
virtual_network_rules
FROM azure.data_lake_analytics.vw_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.data_lake_analytics.accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>accounts</code> resource.

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
INSERT INTO azure.data_lake_analytics.accounts (
accountName,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: defaultDataLakeStoreAccount
          value: string
        - name: dataLakeStoreAccounts
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: suffix
                    value: string
        - name: storageAccounts
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: accessKey
                    value: string
                  - name: suffix
                    value: string
        - name: computePolicies
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: objectId
                    value: string
                  - name: objectType
                    value: string
                  - name: maxDegreeOfParallelismPerJob
                    value: integer
                  - name: minPriorityPerJob
                    value: integer
        - name: firewallRules
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: startIpAddress
                    value: string
                  - name: endIpAddress
                    value: string
        - name: firewallState
          value: string
        - name: firewallAllowAzureIps
          value: string
        - name: newTier
          value: string
        - name: maxJobCount
          value: integer
        - name: maxDegreeOfParallelism
          value: integer
        - name: maxDegreeOfParallelismPerJob
          value: integer
        - name: minPriorityPerJob
          value: integer
        - name: queryStoreRetention
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>accounts</code> resource.

```sql
/*+ update */
UPDATE azure.data_lake_analytics.accounts
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_lake_analytics.accounts
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
