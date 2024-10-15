---
title: regulatory_compliance_standards
hide_title: false
hide_table_of_contents: false
keywords:
  - regulatory_compliance_standards
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

Creates, updates, deletes, gets or lists a <code>regulatory_compliance_standards</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regulatory_compliance_standards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.regulatory_compliance_standards" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_regulatory_compliance_standards', value: 'view', },
        { label: 'regulatory_compliance_standards', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="failed_controls" /> | `text` | field from the `properties` object |
| <CopyableCode code="passed_controls" /> | `text` | field from the `properties` object |
| <CopyableCode code="regulatoryComplianceStandardName" /> | `text` | field from the `properties` object |
| <CopyableCode code="skipped_controls" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="unsupported_controls" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Regulatory compliance standard data |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="regulatoryComplianceStandardName, subscriptionId" /> | Supported regulatory compliance details state for selected standard |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Supported regulatory compliance standards details and state |

## `SELECT` examples

Supported regulatory compliance standards details and state

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_regulatory_compliance_standards', value: 'view', },
        { label: 'regulatory_compliance_standards', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
failed_controls,
passed_controls,
regulatoryComplianceStandardName,
skipped_controls,
state,
subscriptionId,
type,
unsupported_controls
FROM azure.security.vw_regulatory_compliance_standards
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.regulatory_compliance_standards
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

