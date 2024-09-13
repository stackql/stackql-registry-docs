---
title: xpn_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - xpn_resources
  - compute
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

Creates, updates, deletes, gets or lists a <code>xpn_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>xpn_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.xpn_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the service resource. In the case of projects, this field supports project id (e.g., my-project-123) and project number (e.g. 12345678). |
| <CopyableCode code="type" /> | `string` | The type of the service resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_xpn_resources" /> | `SELECT` | <CopyableCode code="project" /> | Gets service resources (a.k.a service project) associated with this host project. |

## `SELECT` examples

Gets service resources (a.k.a service project) associated with this host project.

```sql
SELECT
id,
type
FROM google.compute.xpn_resources
WHERE project = '{{ project }}'; 
```
