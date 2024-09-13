---
title: keys_key_string
hide_title: false
hide_table_of_contents: false
keywords:
  - keys_key_string
  - apikeys
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

Creates, updates, deletes or gets an <code>keys_key_string</code> resource or lists <code>keys_key_string</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys_key_string</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apikeys.keys_key_string" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="keyString" /> | `string` | An encrypted and signed value of the key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_key_string" /> | `SELECT` | <CopyableCode code="keysId, locationsId, projectsId" /> | Get the key string for an API key. NOTE: Key is a global resource; hence the only supported value for location is `global`. |

## `SELECT` examples

Get the key string for an API key. NOTE: Key is a global resource; hence the only supported value for location is `global`.

```sql
SELECT
keyString
FROM google.apikeys.keys_key_string
WHERE keysId = '{{ keysId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
