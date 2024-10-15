---
title: scoping_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - scoping_configurations
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

Creates, updates, deletes, gets or lists a <code>scoping_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scoping_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.scoping_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scoping_configurations', value: 'view', },
        { label: 'scoping_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="answers" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reportName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopingConfigurationName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | ScopingConfiguration's properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="reportName, scopingConfigurationName" /> | Get the AppComplianceAutomation scoping configuration of the specific report. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="reportName" /> | Returns a list format of the singleton scopingConfiguration for a specified report. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="reportName, scopingConfigurationName, data__properties" /> | Get the AppComplianceAutomation scoping configuration of the specific report. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="reportName, scopingConfigurationName" /> | Clean the AppComplianceAutomation scoping configuration of the specific report. |

## `SELECT` examples

Returns a list format of the singleton scopingConfiguration for a specified report.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scoping_configurations', value: 'view', },
        { label: 'scoping_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
answers,
provisioning_state,
reportName,
scopingConfigurationName
FROM azure_extras.app_compliance_automation.vw_scoping_configurations
WHERE reportName = '{{ reportName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.app_compliance_automation.scoping_configurations
WHERE reportName = '{{ reportName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scoping_configurations</code> resource.

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
INSERT INTO azure_extras.app_compliance_automation.scoping_configurations (
reportName,
scopingConfigurationName,
data__properties,
properties
)
SELECT 
'{{ reportName }}',
'{{ scopingConfigurationName }}',
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
        - name: answers
          value:
            - - name: questionId
                value: string
              - name: answers
                value:
                  - string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>scoping_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.app_compliance_automation.scoping_configurations
WHERE reportName = '{{ reportName }}'
AND scopingConfigurationName = '{{ scopingConfigurationName }}';
```
