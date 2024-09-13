---
title: instances_shielded_instance_identity
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_shielded_instance_identity
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

Creates, updates, deletes, gets or lists a <code>instances_shielded_instance_identity</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_shielded_instance_identity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instances_shielded_instance_identity" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="encryptionKey" /> | `object` | A Shielded Instance Identity Entry. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#shieldedInstanceIdentity for shielded Instance identity entry. |
| <CopyableCode code="signingKey" /> | `object` | A Shielded Instance Identity Entry. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_shielded_instance_identity" /> | `SELECT` | <CopyableCode code="instance, project, zone" /> | Returns the Shielded Instance Identity of an instance |

## `SELECT` examples

Returns the Shielded Instance Identity of an instance

```sql
SELECT
encryptionKey,
kind,
signingKey
FROM google.compute.instances_shielded_instance_identity
WHERE instance = '{{ instance }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}'; 
```
