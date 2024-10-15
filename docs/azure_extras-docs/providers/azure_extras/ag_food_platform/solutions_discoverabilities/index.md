---
title: solutions_discoverabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions_discoverabilities
  - ag_food_platform
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

Creates, updates, deletes, gets or lists a <code>solutions_discoverabilities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>solutions_discoverabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.ag_food_platform.solutions_discoverabilities" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solutions_discoverabilities', value: 'view', },
        { label: 'solutions_discoverabilities', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="access_fb_application_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="access_fb_application_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="action_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataManagerForAgricultureSolutionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_access_scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="marketplace_offer_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="open_api_specs_dictionary" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="saa_s_application_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | DataManagerForAgricultureSolution properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerForAgricultureSolutionId" /> | Get Data Manager For Agriculture solution by id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Get list of Data Manager For Agriculture solutions. |

## `SELECT` examples

Get list of Data Manager For Agriculture solutions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solutions_discoverabilities', value: 'view', },
        { label: 'solutions_discoverabilities', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
access_fb_application_id,
access_fb_application_name,
action_ids,
dataManagerForAgricultureSolutionId,
data_access_scopes,
marketplace_offer_details,
open_api_specs_dictionary,
partner_id,
partner_tenant_id,
role_id,
role_name,
saa_s_application_id,
system_data
FROM azure_extras.ag_food_platform.vw_solutions_discoverabilities
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure_extras.ag_food_platform.solutions_discoverabilities
;
```
</TabItem></Tabs>

