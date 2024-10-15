---
title: server_configuration_options
hide_title: false
hide_table_of_contents: false
keywords:
  - server_configuration_options
  - sql
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

Creates, updates, deletes, gets or lists a <code>server_configuration_options</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_configuration_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_configuration_options" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_configuration_options', value: 'view', },
        { label: 'server_configuration_options', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverConfigurationOptionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_configuration_option_value" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of server configuration option. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, serverConfigurationOptionName, subscriptionId" /> | Gets managed instance server configuration option. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedInstanceName, resourceGroupName, serverConfigurationOptionName, subscriptionId" /> | Updates managed instance server configuration option. |

## `SELECT` examples

Gets managed instance server configuration option.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_configuration_options', value: 'view', },
        { label: 'server_configuration_options', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
managedInstanceName,
provisioning_state,
resourceGroupName,
serverConfigurationOptionName,
server_configuration_option_value,
subscriptionId
FROM azure.sql.vw_server_configuration_options
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverConfigurationOptionName = '{{ serverConfigurationOptionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.server_configuration_options
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverConfigurationOptionName = '{{ serverConfigurationOptionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_configuration_options</code> resource.

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
INSERT INTO azure.sql.server_configuration_options (
managedInstanceName,
resourceGroupName,
serverConfigurationOptionName,
subscriptionId,
properties
)
SELECT 
'{{ managedInstanceName }}',
'{{ resourceGroupName }}',
'{{ serverConfigurationOptionName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: serverConfigurationOptionValue
          value: integer
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>
