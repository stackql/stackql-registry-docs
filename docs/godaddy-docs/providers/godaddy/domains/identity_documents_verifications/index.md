---
title: identity_documents_verifications
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_documents_verifications
  - domains
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_documents_verifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="godaddy.domains.identity_documents_verifications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="createdAt" /> | `string` | Timestamp indicating when the user created the identity document verification job |
| <CopyableCode code="status" /> | `string` |  |
| <CopyableCode code="tld" /> | `string` | Top level domain the current identity document verification is for |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_identity_document_verification" /> | `SELECT` | <CopyableCode code="identity_document_id" /> | Retrieve a list of Verifications for the specified Identity Document |
| <CopyableCode code="create_verification" /> | `INSERT` | <CopyableCode code="identity_document_id, tlds" /> | Only one verification job is needed for one TLD, Top Level Domain, per identity document. Sending in request(s) with multiple domains for the same TLD, will not create multiple verification jobs. We accept domain names for the convenience of our customers so that they don't need to worry about parsing TLDs out of domain names |
