---
title: relyingparty_oob_confirmation_code
hide_title: false
hide_table_of_contents: false
keywords:
  - relyingparty_oob_confirmation_code
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

Creates, updates, deletes, gets or lists a <code>relyingparty_oob_confirmation_code</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relyingparty_oob_confirmation_code</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.identitytoolkit.relyingparty_oob_confirmation_code" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="email" /> | `string` | The email address that the email is sent to. |
| <CopyableCode code="kind" /> | `string` | The fixed string "identitytoolkit#GetOobConfirmationCodeResponse". |
| <CopyableCode code="oobCode" /> | `string` | The code to be send to the user. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_oob_confirmation_code" /> | `SELECT` | <CopyableCode code="" /> | Get a code for user action confirmation. |

## `SELECT` examples

Get a code for user action confirmation.

```sql
SELECT
email,
kind,
oobCode
FROM google.identitytoolkit.relyingparty_oob_confirmation_code
WHERE  = '{{  }}'; 
```
