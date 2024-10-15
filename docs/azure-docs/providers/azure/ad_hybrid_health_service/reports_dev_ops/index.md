---
title: reports_dev_ops
hide_title: false
hide_table_of_contents: false
keywords:
  - reports_dev_ops
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

Creates, updates, deletes, gets or lists a <code>reports_dev_ops</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports_dev_ops</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.reports_dev_ops" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="value" /> | `boolean` | The value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> | Checks if the user is enabled for Dev Ops access. |

## `SELECT` examples

Checks if the user is enabled for Dev Ops access.


```sql
SELECT
value
FROM azure.ad_hybrid_health_service.reports_dev_ops
;
```