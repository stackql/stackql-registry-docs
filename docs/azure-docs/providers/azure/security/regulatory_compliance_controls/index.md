---
title: regulatory_compliance_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - regulatory_compliance_controls
  - security
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

Creates, updates, deletes, gets or lists a <code>regulatory_compliance_controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regulatory_compliance_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.regulatory_compliance_controls" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_regulatory_compliance_controls', value: 'view', },
        { label: 'regulatory_compliance_controls', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="failed_assessments" /> | `text` | field from the `properties` object |
| <CopyableCode code="passed_assessments" /> | `text` | field from the `properties` object |
| <CopyableCode code="regulatoryComplianceControlName" /> | `text` | field from the `properties` object |
| <CopyableCode code="regulatoryComplianceStandardName" /> | `text` | field from the `properties` object |
| <CopyableCode code="skipped_assessments" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Regulatory compliance control data |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="regulatoryComplianceControlName, regulatoryComplianceStandardName, subscriptionId" /> | Selected regulatory compliance control details and state |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="regulatoryComplianceStandardName, subscriptionId" /> | All supported regulatory compliance controls details and state for selected standard |

## `SELECT` examples

All supported regulatory compliance controls details and state for selected standard

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_regulatory_compliance_controls', value: 'view', },
        { label: 'regulatory_compliance_controls', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
failed_assessments,
passed_assessments,
regulatoryComplianceControlName,
regulatoryComplianceStandardName,
skipped_assessments,
state,
subscriptionId,
type
FROM azure.security.vw_regulatory_compliance_controls
WHERE regulatoryComplianceStandardName = '{{ regulatoryComplianceStandardName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.regulatory_compliance_controls
WHERE regulatoryComplianceStandardName = '{{ regulatoryComplianceStandardName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

