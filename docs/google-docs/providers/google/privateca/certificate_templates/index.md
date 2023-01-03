---
title: certificate_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_templates
  - privateca
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
<tr><td><b>Name</b></td><td><code>certificate_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.privateca.certificate_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for this CertificateTemplate in the format `projects/*/locations/*/certificateTemplates/*`. |
| `description` | `string` | Optional. A human-readable description of scenarios this template is intended for. |
| `identityConstraints` | `object` | Describes constraints on a Certificate's Subject and SubjectAltNames. |
| `labels` | `object` | Optional. Labels with user-defined metadata. |
| `passthroughExtensions` | `object` | Describes a set of X.509 extensions that may be part of some certificate issuance controls. |
| `predefinedValues` | `object` | An X509Parameters is used to describe certain fields of an X.509 certificate, such as the key usage fields, fields specific to CA certificates, certificate policy extensions and custom extensions. |
| `updateTime` | `string` | Output only. The time at which this CertificateTemplate was updated. |
| `createTime` | `string` | Output only. The time at which this CertificateTemplate was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_certificateTemplates_get` | `SELECT` | `certificateTemplatesId, locationsId, projectsId` | Returns a CertificateTemplate. |
| `projects_locations_certificateTemplates_list` | `SELECT` | `locationsId, projectsId` | Lists CertificateTemplates. |
| `projects_locations_certificateTemplates_create` | `INSERT` | `locationsId, projectsId` | Create a new CertificateTemplate in a given Project and Location. |
| `projects_locations_certificateTemplates_delete` | `DELETE` | `certificateTemplatesId, locationsId, projectsId` | DeleteCertificateTemplate deletes a CertificateTemplate. |
| `projects_locations_certificateTemplates_patch` | `EXEC` | `certificateTemplatesId, locationsId, projectsId` | Update a CertificateTemplate. |
