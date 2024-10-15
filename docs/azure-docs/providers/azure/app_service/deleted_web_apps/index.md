---
title: deleted_web_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_web_apps
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

Creates, updates, deletes, gets or lists a <code>deleted_web_apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deleted_web_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.deleted_web_apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | DeletedSite resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_location" /> | `SELECT` | <CopyableCode code="deletedSiteId, location, subscriptionId" /> | Description for Get deleted app for a subscription at location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Get all deleted apps for a subscription. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Description for Get all deleted apps for a subscription at location |

## `SELECT` examples

Description for Get all deleted apps for a subscription.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.deleted_web_apps
WHERE subscriptionId = '{{ subscriptionId }}';
```