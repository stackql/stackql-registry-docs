---
title: runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - runtimes
  - cloudfunctions
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

Creates, updates, deletes, gets or lists a <code>runtimes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudfunctions.runtimes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="runtimes" /> | `array` | The runtimes that match the request. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns a list of runtimes that are supported for the requested project. |

## `SELECT` examples

Returns a list of runtimes that are supported for the requested project.

```sql
SELECT
runtimes
FROM google.cloudfunctions.runtimes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
