---
title: diagnostics_site_diagnostic_category_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostics_site_diagnostic_category_slots
  - app_service
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

Creates, updates, deletes, gets or lists a <code>diagnostics_site_diagnostic_category_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>diagnostics_site_diagnostic_category_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.diagnostics_site_diagnostic_category_slots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | DiagnosticCategory resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diagnosticCategory, resourceGroupName, siteName, slot, subscriptionId" /> | Description for Get Diagnostics Category |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, slot, subscriptionId" /> | Description for Get Diagnostics Categories |

## `SELECT` examples

Description for Get Diagnostics Categories


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.diagnostics_site_diagnostic_category_slots
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```