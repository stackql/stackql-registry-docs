
---
title: info_types
hide_title: false
hide_table_of_contents: false
keywords:
  - info_types
  - dlp
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

Creates, updates, deletes or gets an <code>info_type</code> resource or lists <code>info_types</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>info_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dlp.info_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="infoTypes" /> | `array` | Set of sensitive infoTypes. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="info_types_list" /> | `SELECT` | <CopyableCode code="" /> | Returns a list of the sensitive information types that DLP API supports. See https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference to learn more. |
| <CopyableCode code="locations_info_types_list" /> | `SELECT` | <CopyableCode code="locationsId" /> | Returns a list of the sensitive information types that DLP API supports. See https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference to learn more. |

## `SELECT` examples

Returns a list of the sensitive information types that DLP API supports. See https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference to learn more.

```sql
SELECT
infoTypes
FROM google.dlp.info_types
WHERE  = '{{  }}'; 
```
