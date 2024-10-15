---
title: services_export_errors
hide_title: false
hide_table_of_contents: false
keywords:
  - services_export_errors
  - ad_hybrid_health_service
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

Creates, updates, deletes, gets or lists a <code>services_export_errors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services_export_errors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services_export_errors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="count" /> | `integer` | The error count. |
| <CopyableCode code="errorBucket" /> | `string` | The error bucket. |
| <CopyableCode code="truncated" /> | `boolean` | Indicates if the error count is truncated or not. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets the count of latest AAD export errors. |

## `SELECT` examples

Gets the count of latest AAD export errors.


```sql
SELECT
count,
errorBucket,
truncated
FROM azure.ad_hybrid_health_service.services_export_errors
WHERE serviceName = '{{ serviceName }}';
```