---
title: relyingparty_account_info
hide_title: false
hide_table_of_contents: false
keywords:
  - relyingparty_account_info
  - identitytoolkit
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

Creates, updates, deletes, gets or lists a <code>relyingparty_account_info</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relyingparty_account_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.identitytoolkit.relyingparty_account_info" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | The fixed string "identitytoolkit#GetAccountInfoResponse". |
| <CopyableCode code="users" /> | `array` | The info of the users. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_account_info" /> | `SELECT` | <CopyableCode code="" /> | Returns the account info. |

## `SELECT` examples

Returns the account info.

```sql
SELECT
kind,
users
FROM google.identitytoolkit.relyingparty_account_info
WHERE  = '{{  }}'; 
```
