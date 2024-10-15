---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - openshift_clusters
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

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.openshift_clusters.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Operation name: {provider}/{resource}/{operation}. |
| <CopyableCode code="display" /> | `object` | Display represents the display details of an operation. |
| <CopyableCode code="origin" /> | `string` | Sources of requests to this operation.  Comma separated list with valid values user or system, e.g. "user,system". |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | The operation returns the RP operations. |

## `SELECT` examples

The operation returns the RP operations.


```sql
SELECT
name,
display,
origin
FROM azure_isv.openshift_clusters.operations
;
```