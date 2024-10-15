---
title: dsc_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_configurations
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

Creates, updates, deletes, gets or lists a <code>dsc_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dsc_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.dsc_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dsc_configurations', value: 'view', },
        { label: 'dsc_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Gets or sets the etag of the resource. |
| <CopyableCode code="job_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="log_verbose" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_configuration_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Gets or sets the etag of the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Definition of the configuration property type. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, configurationName, resourceGroupName, subscriptionId" /> | Retrieve the configuration identified by configuration name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of configurations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, configurationName, resourceGroupName, subscriptionId, data__properties" /> | Create the configuration identified by configuration name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, configurationName, resourceGroupName, subscriptionId" /> | Delete the dsc configuration identified by configuration name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="automationAccountName, configurationName, resourceGroupName, subscriptionId" /> | Create the configuration identified by configuration name. |

## `SELECT` examples

Retrieve a list of configurations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dsc_configurations', value: 'view', },
        { label: 'dsc_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
automationAccountName,
configurationName,
creation_time,
etag,
job_count,
last_modified_time,
location,
log_verbose,
node_configuration_count,
parameters,
provisioning_state,
resourceGroupName,
source,
state,
subscriptionId,
tags
FROM azure.automation.vw_dsc_configurations
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
tags
FROM azure.automation.dsc_configurations
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dsc_configurations</code> resource.

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
INSERT INTO azure.automation.dsc_configurations (
automationAccountName,
configurationName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
name,
location,
tags
)
SELECT 
'{{ automationAccountName }}',
'{{ configurationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ name }}',
'{{ location }}',
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
        - name: logVerbose
          value: boolean
        - name: logProgress
          value: boolean
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
        - name: parameters
          value: object
        - name: description
          value: string
    - name: name
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dsc_configurations</code> resource.

```sql
/*+ update */
UPDATE azure.automation.dsc_configurations
SET 
properties = '{{ properties }}',
name = '{{ name }}',
tags = '{{ tags }}'
WHERE 
automationAccountName = '{{ automationAccountName }}'
AND configurationName = '{{ configurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>dsc_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.dsc_configurations
WHERE automationAccountName = '{{ automationAccountName }}'
AND configurationName = '{{ configurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
