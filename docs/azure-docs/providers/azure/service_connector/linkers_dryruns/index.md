---
title: linkers_dryruns
hide_title: false
hide_table_of_contents: false
keywords:
  - linkers_dryruns
  - service_connector
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

Creates, updates, deletes, gets or lists a <code>linkers_dryruns</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>linkers_dryruns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_connector.linkers_dryruns" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_linkers_dryruns', value: 'view', },
        { label: 'linkers_dryruns', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dryrunName" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation_previews" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="prerequisite_results" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of the dryrun job |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dryrunName, resourceUri" /> | get a dryrun job |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | list dryrun jobs |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dryrunName, resourceUri" /> | create a dryrun job to do necessary check before actual creation |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dryrunName, resourceUri" /> | delete a dryrun job |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dryrunName, resourceUri" /> | add a dryrun job to do necessary check before actual creation |

## `SELECT` examples

list dryrun jobs

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_linkers_dryruns', value: 'view', },
        { label: 'linkers_dryruns', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dryrunName,
operation_previews,
parameters,
prerequisite_results,
provisioning_state,
resourceUri
FROM azure.service_connector.vw_linkers_dryruns
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.service_connector.linkers_dryruns
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>linkers_dryruns</code> resource.

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
INSERT INTO azure.service_connector.linkers_dryruns (
dryrunName,
resourceUri,
properties
)
SELECT 
'{{ dryrunName }}',
'{{ resourceUri }}',
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
        - name: parameters
          value:
            - name: actionName
              value: []
        - name: prerequisiteResults
          value:
            - - name: type
                value: []
        - name: operationPreviews
          value:
            - - name: name
                value: string
              - name: operationType
                value: string
              - name: description
                value: string
              - name: action
                value: string
              - name: scope
                value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>linkers_dryruns</code> resource.

```sql
/*+ update */
UPDATE azure.service_connector.linkers_dryruns
SET 
properties = '{{ properties }}'
WHERE 
dryrunName = '{{ dryrunName }}'
AND resourceUri = '{{ resourceUri }}';
```

## `DELETE` example

Deletes the specified <code>linkers_dryruns</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_connector.linkers_dryruns
WHERE dryrunName = '{{ dryrunName }}'
AND resourceUri = '{{ resourceUri }}';
```
