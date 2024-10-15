---
title: evidences
hide_title: false
hide_table_of_contents: false
keywords:
  - evidences
  - app_compliance_automation
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

Creates, updates, deletes, gets or lists a <code>evidences</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>evidences</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.evidences" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_evidences', value: 'view', },
        { label: 'evidences', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="control_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="evidenceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="evidence_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="extra_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reportName" /> | `text` | field from the `properties` object |
| <CopyableCode code="responsibility_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Evidence's properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="evidenceName, reportName" /> | Get the evidence metadata |
| <CopyableCode code="list_by_report" /> | `SELECT` | <CopyableCode code="reportName" /> | Returns a paginated list of evidences for a specified report. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="evidenceName, reportName, data__properties" /> | Create or Update an evidence a specified report |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="evidenceName, reportName" /> | Delete an existent evidence from a specified report |
| <CopyableCode code="download" /> | `EXEC` | <CopyableCode code="evidenceName, reportName" /> | Download evidence file. |

## `SELECT` examples

Returns a paginated list of evidences for a specified report.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_evidences', value: 'view', },
        { label: 'evidences', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
control_id,
evidenceName,
evidence_type,
extra_data,
file_path,
provisioning_state,
reportName,
responsibility_id
FROM azure_extras.app_compliance_automation.vw_evidences
WHERE reportName = '{{ reportName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.app_compliance_automation.evidences
WHERE reportName = '{{ reportName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>evidences</code> resource.

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
INSERT INTO azure_extras.app_compliance_automation.evidences (
evidenceName,
reportName,
data__properties,
properties
)
SELECT 
'{{ evidenceName }}',
'{{ reportName }}',
'{{ data__properties }}',
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
        - name: evidenceType
          value: []
        - name: filePath
          value: string
        - name: extraData
          value: string
        - name: controlId
          value: string
        - name: responsibilityId
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>evidences</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.app_compliance_automation.evidences
WHERE evidenceName = '{{ evidenceName }}'
AND reportName = '{{ reportName }}';
```
