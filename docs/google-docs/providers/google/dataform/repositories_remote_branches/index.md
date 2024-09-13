---
title: repositories_remote_branches
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories_remote_branches
  - dataform
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

Creates, updates, deletes or gets an <code>repositories_remote_branch</code> resource or lists <code>repositories_remote_branches</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories_remote_branches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataform.repositories_remote_branches" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="branches" /> | `array` | The remote repository's branch names. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_remote_branches" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Fetches a Repository's remote branches. |

## `SELECT` examples

Fetches a Repository's remote branches.

```sql
SELECT
branches
FROM google.dataform.repositories_remote_branches
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'; 
```
