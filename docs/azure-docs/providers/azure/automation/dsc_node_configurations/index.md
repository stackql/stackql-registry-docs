---
title: dsc_node_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_node_configurations
  - automation
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

Creates, updates, deletes, gets or lists a <code>dsc_node_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dsc_node_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.dsc_node_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dsc_node_configurations', value: 'view', },
        { label: 'dsc_node_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="increment_node_configuration_build" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="nodeConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties for the DscNodeConfiguration |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, nodeConfigurationName, resourceGroupName, subscriptionId" /> | Retrieve the Dsc node configurations by node configuration. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of dsc node configurations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, nodeConfigurationName, resourceGroupName, subscriptionId" /> | Create the node configuration identified by node configuration name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, nodeConfigurationName, resourceGroupName, subscriptionId" /> | Delete the Dsc node configurations by node configuration. |

## `SELECT` examples

Retrieve a list of dsc node configurations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dsc_node_configurations', value: 'view', },
        { label: 'dsc_node_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
automationAccountName,
configuration,
creation_time,
increment_node_configuration_build,
last_modified_time,
nodeConfigurationName,
node_count,
resourceGroupName,
source,
subscriptionId
FROM azure.automation.vw_dsc_node_configurations
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.automation.dsc_node_configurations
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dsc_node_configurations</code> resource.

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
INSERT INTO azure.automation.dsc_node_configurations (
automationAccountName,
nodeConfigurationName,
resourceGroupName,
subscriptionId,
properties,
name,
tags
)
SELECT 
'{{ automationAccountName }}',
'{{ nodeConfigurationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ name }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: source
          value:
            - name: hash
              value:
                - name: algorithm
                  value: string
                - name: value
                  value: string
            - name: type
              value: string
            - name: value
              value: string
            - name: version
              value: string
        - name: configuration
          value:
            - name: name
              value: string
        - name: incrementNodeConfigurationBuild
          value: boolean
    - name: name
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dsc_node_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.dsc_node_configurations
WHERE automationAccountName = '{{ automationAccountName }}'
AND nodeConfigurationName = '{{ nodeConfigurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
