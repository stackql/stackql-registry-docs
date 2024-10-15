---
title: error_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - error_summaries
  - off_azure_springboot
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

Creates, updates, deletes, gets or lists a <code>error_summaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>error_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.off_azure_springboot.error_summaries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_error_summaries', value: 'view', },
        { label: 'error_summaries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="discovery_scope_error_summaries" /> | `text` | field from the `properties` object |
| <CopyableCode code="errorSummaryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Error summary properties |
| <CopyableCode code="tags" /> | `object` | Resource tags |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="errorSummaryName, resourceGroupName, siteName, subscriptionId" /> | Gets the ErrorSummaries resource. |
| <CopyableCode code="list_by_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Lists the ErrorSummaries resource in springbootsites. |

## `SELECT` examples

Lists the ErrorSummaries resource in springbootsites.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_error_summaries', value: 'view', },
        { label: 'error_summaries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
discovery_scope_error_summaries,
errorSummaryName,
errors,
provisioning_state,
resourceGroupName,
siteName,
subscriptionId,
tags
FROM azure_extras.off_azure_springboot.vw_error_summaries
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure_extras.off_azure_springboot.error_summaries
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

