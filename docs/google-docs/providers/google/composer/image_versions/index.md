---
title: image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - image_versions
  - composer
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
<tr><td><b>Name</b></td><td><code>image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.composer.image_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `imageVersionId` | `string` | The string identifier of the ImageVersion, in the form: "composer-x.y.z-airflow-a.b.c" |
| `isDefault` | `boolean` | Whether this is the default ImageVersion used by Composer during environment creation if no input ImageVersion is specified. |
| `releaseDate` | `object` | Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp |
| `supportedPythonVersions` | `array` | supported python versions |
| `upgradeDisabled` | `boolean` | Whether it is impossible to upgrade an environment running with the image version. |
| `creationDisabled` | `boolean` | Whether it is impossible to create an environment with the image version. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_imageVersions_list` | `SELECT` | `locationsId, projectsId` |
