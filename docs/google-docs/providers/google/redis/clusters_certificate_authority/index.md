
---
title: clusters_certificate_authority
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_certificate_authority
  - redis
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

Creates, updates, deletes or gets an <code>clusters_certificate_authority</code> resource or lists <code>clusters_certificate_authority</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_certificate_authority</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.redis.clusters_certificate_authority" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Unique name of the resource in this scope including project, location and cluster using the form: `projects/{project}/locations/{location}/clusters/{cluster}/certificateAuthority` |
| <CopyableCode code="managedServerCa" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_certificate_authority" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Gets the details of certificate authority information for Redis cluster. |

## `SELECT` examples

Gets the details of certificate authority information for Redis cluster.

```sql
SELECT
name,
managedServerCa
FROM google.redis.clusters_certificate_authority
WHERE clustersId = '{{ clustersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
