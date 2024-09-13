
---
title: keys_legacy_secret_key
hide_title: false
hide_table_of_contents: false
keywords:
  - keys_legacy_secret_key
  - recaptchaenterprise
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

Creates, updates, deletes or gets an <code>keys_legacy_secret_key</code> resource or lists <code>keys_legacy_secret_key</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys_legacy_secret_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recaptchaenterprise.keys_legacy_secret_key" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="legacySecretKey" /> | `string` | The secret key (also known as shared secret) authorizes communication between your application backend and the reCAPTCHA Enterprise server to create an assessment. The secret key needs to be kept safe for security purposes. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="retrieve_legacy_secret_key" /> | `SELECT` | <CopyableCode code="keysId, projectsId" /> | Returns the secret key related to the specified public key. You must use the legacy secret key only in a 3rd party integration with legacy reCAPTCHA. |

## `SELECT` examples

Returns the secret key related to the specified public key. You must use the legacy secret key only in a 3rd party integration with legacy reCAPTCHA.

```sql
SELECT
legacySecretKey
FROM google.recaptchaenterprise.keys_legacy_secret_key
WHERE keysId = '{{ keysId }}'
AND projectsId = '{{ projectsId }}'; 
```
