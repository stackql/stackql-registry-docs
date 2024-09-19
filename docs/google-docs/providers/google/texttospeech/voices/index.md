---
title: voices
hide_title: false
hide_table_of_contents: false
keywords:
  - voices
  - texttospeech
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

Creates, updates, deletes, gets or lists a <code>voices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>voices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.texttospeech.voices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="voices" /> | `array` | The list of voices. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Returns a list of Voice supported for synthesis. |

## `SELECT` examples

Returns a list of Voice supported for synthesis.

```sql
SELECT
voices
FROM google.texttospeech.voices
;
```
