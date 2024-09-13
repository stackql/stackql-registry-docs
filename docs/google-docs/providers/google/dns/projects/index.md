
---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - dns
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

Creates, updates, deletes or gets an <code>project</code> resource or lists <code>projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dns.projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | User assigned unique identifier for the resource (output only). |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="number" /> | `string` | Unique numeric identifier for the resource; defined by the server (output only). |
| <CopyableCode code="quota" /> | `object` | Limits associated with a Project. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project" /> | Fetches the representation of an existing Project. |

## `SELECT` examples

Fetches the representation of an existing Project.

```sql
SELECT
id,
kind,
number,
quota
FROM google.dns.projects
WHERE project = '{{ project }}'; 
```
