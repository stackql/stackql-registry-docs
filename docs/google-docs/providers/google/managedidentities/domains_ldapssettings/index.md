---
title: domains_ldapssettings
hide_title: false
hide_table_of_contents: false
keywords:
  - domains_ldapssettings
  - managedidentities
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains_ldapssettings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.managedidentities.domains_ldapssettings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the LDAPS settings. Uses the form: `projects/{project}/locations/{location}/domains/{domain}`. |
| `certificate` | `object` | Certificate used to configure LDAPS. |
| `certificatePassword` | `string` | Input only. The password used to encrypt the uploaded PFX certificate. |
| `certificatePfx` | `string` | Input only. The uploaded PKCS12-formatted certificate to configure LDAPS with. It will enable the domain controllers in this domain to accept LDAPS connections (either LDAP over SSL/TLS or the StartTLS operation). A valid certificate chain must form a valid x.509 certificate chain (or be comprised of a single self-signed certificate. It must be encrypted with either: 1) PBES2 + PBKDF2 + AES256 encryption and SHA256 PRF; or 2) pbeWithSHA1And3-KeyTripleDES-CBC Private key must be included for the leaf / single self-signed certificate. Note: For a fqdn your-example-domain.com, the wildcard fqdn is *.your-example-domain.com. Specifically the leaf certificate must have: - Either a blank subject or a subject with CN matching the wildcard fqdn. - Exactly two SANs - the fqdn and wildcard fqdn. - Encipherment and digital key signature key usages. - Server authentication extended key usage (OID=1.3.6.1.5.5.7.3.1) - Private key must be in one of the following formats: RSA, ECDSA, ED25519. - Private key must have appropriate key length: 2048 for RSA, 256 for ECDSA - Signature algorithm of the leaf certificate cannot be MD2, MD5 or SHA1. |
| `state` | `string` | Output only. The current state of this LDAPS settings. |
| `updateTime` | `string` | Output only. Last update time. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_global_domains_getLdapssettings` | `SELECT` | `domainsId, projectsId` |
