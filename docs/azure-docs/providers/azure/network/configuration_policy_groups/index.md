---
title: configuration_policy_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_policy_groups
  - network
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

Creates, updates, deletes, gets or lists a <code>configuration_policy_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_policy_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.configuration_policy_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_policy_groups', value: 'view', },
        { label: 'configuration_policy_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="configurationPolicyGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="is_default" /> | `text` | field from the `properties` object |
| <CopyableCode code="p2_s_connection_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_members" /> | `text` | field from the `properties` object |
| <CopyableCode code="priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="vpnServerConfigurationName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Parameters for VpnServerConfigurationPolicyGroup. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationPolicyGroupName, resourceGroupName, subscriptionId, vpnServerConfigurationName" /> | Retrieves the details of a ConfigurationPolicyGroup. |
| <CopyableCode code="list_by_vpn_server_configuration" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vpnServerConfigurationName" /> | Lists all the configurationPolicyGroups in a resource group for a vpnServerConfiguration. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationPolicyGroupName, resourceGroupName, subscriptionId, vpnServerConfigurationName" /> | Creates a ConfigurationPolicyGroup if it doesn't exist else updates the existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationPolicyGroupName, resourceGroupName, subscriptionId, vpnServerConfigurationName" /> | Deletes a ConfigurationPolicyGroup. |

## `SELECT` examples

Lists all the configurationPolicyGroups in a resource group for a vpnServerConfiguration.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_policy_groups', value: 'view', },
        { label: 'configuration_policy_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
configurationPolicyGroupName,
etag,
is_default,
p2_s_connection_configurations,
policy_members,
priority,
provisioning_state,
resourceGroupName,
subscriptionId,
type,
vpnServerConfigurationName
FROM azure.network.vw_configuration_policy_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vpnServerConfigurationName = '{{ vpnServerConfigurationName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.network.configuration_policy_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vpnServerConfigurationName = '{{ vpnServerConfigurationName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_policy_groups</code> resource.

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
INSERT INTO azure.network.configuration_policy_groups (
configurationPolicyGroupName,
resourceGroupName,
subscriptionId,
vpnServerConfigurationName,
properties,
name,
id
)
SELECT 
'{{ configurationPolicyGroupName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vpnServerConfigurationName }}',
'{{ properties }}',
'{{ name }}',
'{{ id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: isDefault
          value: boolean
        - name: priority
          value: integer
        - name: policyMembers
          value:
            - - name: name
                value: string
              - name: attributeType
                value: string
              - name: attributeValue
                value: string
        - name: p2SConnectionConfigurations
          value:
            - - name: id
                value: string
        - name: provisioningState
          value: []
    - name: etag
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>configuration_policy_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.configuration_policy_groups
WHERE configurationPolicyGroupName = '{{ configurationPolicyGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vpnServerConfigurationName = '{{ vpnServerConfigurationName }}';
```
