---
title: instances_server_cas
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_server_cas
  - sqladmin
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

Creates, updates, deletes, gets or lists a <code>instances_server_cas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_server_cas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sqladmin.instances_server_cas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activeVersion" /> | `string` |  |
| <CopyableCode code="certs" /> | `array` | List of server CA certificates for the instance. |
| <CopyableCode code="kind" /> | `string` | This is always `sql#instancesListServerCas`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_server_cas" /> | `SELECT` | <CopyableCode code="instance, project" /> | Lists all of the trusted Certificate Authorities (CAs) for the specified instance. There can be up to three CAs listed: the CA that was used to sign the certificate that is currently in use, a CA that has been added but not yet used to sign a certificate, and a CA used to sign a certificate that has previously rotated out. |

## `SELECT` examples

Lists all of the trusted Certificate Authorities (CAs) for the specified instance. There can be up to three CAs listed: the CA that was used to sign the certificate that is currently in use, a CA that has been added but not yet used to sign a certificate, and a CA used to sign a certificate that has previously rotated out.

```sql
SELECT
activeVersion,
certs,
kind
FROM google.sqladmin.instances_server_cas
WHERE instance = '{{ instance }}'
AND project = '{{ project }}';
```
