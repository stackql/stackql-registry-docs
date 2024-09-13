
---
title: shelves
hide_title: false
hide_table_of_contents: false
keywords:
  - shelves
  - libraryagent
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

Creates, updates, deletes or gets an <code>shelf</code> resource or lists <code>shelves</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shelves</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.libraryagent.shelves" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the shelf. Shelf names have the form `shelves/{shelf_id}`. The name is ignored when creating a shelf. |
| <CopyableCode code="theme" /> | `string` | The theme of the shelf |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="shelvesId" /> | Gets a shelf. Returns NOT_FOUND if the shelf does not exist. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists shelves. The order is unspecified but deterministic. Newly created shelves will not necessarily be added to the end of this list. |

## `SELECT` examples

Lists shelves. The order is unspecified but deterministic. Newly created shelves will not necessarily be added to the end of this list.

```sql
SELECT
name,
theme
FROM google.libraryagent.shelves
WHERE  = '{{  }}'; 
```
