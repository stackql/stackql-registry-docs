---
title: credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - credentials
  - kubernetes
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.kubernetes.credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="certificate_authority_data" /> | `string` | A base64 encoding of bytes representing the certificate authority data for accessing the cluster. |
| <CopyableCode code="client_certificate_data" /> | `string` | A base64 encoding of bytes representing the x509 client<br />certificate data for access the cluster. This is only returned for clusters<br />without support for token-based authentication.<br /><br />Newly created Kubernetes clusters do not return credentials using<br />certificate-based authentication. For additional information,<br />[see here](https://www.digitalocean.com/docs/kubernetes/how-to/connect-to-cluster/#authenticate).<br /> |
| <CopyableCode code="client_key_data" /> | `string` | A base64 encoding of bytes representing the x509 client key<br />data for access the cluster. This is only returned for clusters without<br />support for token-based authentication.<br /><br />Newly created Kubernetes clusters do not return credentials using<br />certificate-based authentication. For additional information,<br />[see here](https://www.digitalocean.com/docs/kubernetes/how-to/connect-to-cluster/#authenticate).<br /> |
| <CopyableCode code="expires_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the access token expires. |
| <CopyableCode code="server" /> | `string` | The URL used to access the cluster API server. |
| <CopyableCode code="token" /> | `string` | An access token used to authenticate with the cluster. This is only returned for clusters with support for token-based authentication. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_credentials" /> | `SELECT` | <CopyableCode code="cluster_id" /> |
