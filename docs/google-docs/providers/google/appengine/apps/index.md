---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - appengine
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

Creates, updates, deletes, gets or lists a <code>apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.appengine.apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Identifier of the Application resource. This identifier is equivalent to the project ID of the Google Cloud Platform project where you want to deploy your application. Example: myapp. |
| <CopyableCode code="name" /> | `string` | Output only. Full path to the Application resource in the API. Example: apps/myapp.@OutputOnly |
| <CopyableCode code="authDomain" /> | `string` | Google Apps authentication domain that controls which users can access this application.Defaults to open access for any Google Account. |
| <CopyableCode code="codeBucket" /> | `string` | Output only. Google Cloud Storage bucket that can be used for storing files associated with this application. This bucket is associated with the application and can be used by the gcloud deployment commands.@OutputOnly |
| <CopyableCode code="databaseType" /> | `string` | The type of the Cloud Firestore or Cloud Datastore database associated with this application. |
| <CopyableCode code="defaultBucket" /> | `string` | Output only. Google Cloud Storage bucket that can be used by this application to store content.@OutputOnly |
| <CopyableCode code="defaultCookieExpiration" /> | `string` | Cookie expiration policy for this application. |
| <CopyableCode code="defaultHostname" /> | `string` | Output only. Hostname used to reach this application, as resolved by App Engine.@OutputOnly |
| <CopyableCode code="dispatchRules" /> | `array` | HTTP path dispatch rules for requests to the application that do not explicitly target a service or version. Rules are order-dependent. Up to 20 dispatch rules can be supported. |
| <CopyableCode code="featureSettings" /> | `object` | The feature specific settings to be used in the application. These define behaviors that are user configurable. |
| <CopyableCode code="gcrDomain" /> | `string` | Output only. The Google Container Registry domain used for storing managed build docker images for this application. |
| <CopyableCode code="generatedCustomerMetadata" /> | `object` | Additional Google Generated Customer Metadata, this field won't be provided by default and can be requested by setting the IncludeExtraData field in GetApplicationRequest |
| <CopyableCode code="iap" /> | `object` | Identity-Aware Proxy |
| <CopyableCode code="locationId" /> | `string` | Location from which this application runs. Application instances run out of the data centers in the specified location, which is also where all of the application's end user content is stored.Defaults to us-central.View the list of supported locations (https://cloud.google.com/appengine/docs/locations). |
| <CopyableCode code="serviceAccount" /> | `string` | The service account associated with the application. This is the app-level default identity. If no identity provided during create version, Admin API will fallback to this one. |
| <CopyableCode code="servingStatus" /> | `string` | Serving status of this application. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appsId" /> | Gets information about an application. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates an App Engine application for a Google Cloud Platform project. Required fields: id - The ID of the target Cloud Platform project. location - The region (https://cloud.google.com/appengine/docs/locations) where you want the App Engine application located.For more information about App Engine applications, see Managing Projects, Applications, and Billing (https://cloud.google.com/appengine/docs/standard/python/console/). |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="appsId" /> | Updates the specified Application resource. You can update the following fields: auth_domain - Google authentication domain for controlling user access to the application. default_cookie_expiration - Cookie expiration policy for the application. iap - Identity-Aware Proxy properties for the application. |
| <CopyableCode code="repair" /> | `EXEC` | <CopyableCode code="appsId" /> | Recreates the required App Engine features for the specified App Engine application, for example a Cloud Storage bucket or App Engine service account. Use this method if you receive an error message about a missing feature, for example, Error retrieving the App Engine service account. If you have deleted your App Engine service account, this will not be able to recreate it. Instead, you should attempt to use the IAM undelete API if possible at https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts/undelete?apix_params=%7B"name"%3A"projects%2F-%2FserviceAccounts%2Funique_id"%2C"resource"%3A%7B%7D%7D . If the deletion was recent, the numeric ID can be found in the Cloud Console Activity Log. |

## `SELECT` examples

Gets information about an application.

```sql
SELECT
id,
name,
authDomain,
codeBucket,
databaseType,
defaultBucket,
defaultCookieExpiration,
defaultHostname,
dispatchRules,
featureSettings,
gcrDomain,
generatedCustomerMetadata,
iap,
locationId,
serviceAccount,
servingStatus
FROM google.appengine.apps
WHERE appsId = '{{ appsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apps</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.appengine.apps (
dispatchRules,
authDomain,
locationId,
defaultCookieExpiration,
servingStatus,
serviceAccount,
iap,
databaseType,
featureSettings,
generatedCustomerMetadata
)
SELECT 
'{{ dispatchRules }}',
'{{ authDomain }}',
'{{ locationId }}',
'{{ defaultCookieExpiration }}',
'{{ servingStatus }}',
'{{ serviceAccount }}',
'{{ iap }}',
'{{ databaseType }}',
'{{ featureSettings }}',
'{{ generatedCustomerMetadata }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: id
      value: string
    - name: dispatchRules
      value:
        - - name: domain
            value: string
          - name: path
            value: string
          - name: service
            value: string
    - name: authDomain
      value: string
    - name: locationId
      value: string
    - name: codeBucket
      value: string
    - name: defaultCookieExpiration
      value: string
    - name: servingStatus
      value: string
    - name: defaultHostname
      value: string
    - name: defaultBucket
      value: string
    - name: serviceAccount
      value: string
    - name: iap
      value:
        - name: enabled
          value: boolean
        - name: oauth2ClientId
          value: string
        - name: oauth2ClientSecret
          value: string
        - name: oauth2ClientSecretSha256
          value: string
    - name: gcrDomain
      value: string
    - name: databaseType
      value: string
    - name: featureSettings
      value:
        - name: splitHealthChecks
          value: boolean
        - name: useContainerOptimizedOs
          value: boolean
    - name: generatedCustomerMetadata
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>apps</code> resource.

```sql
/*+ update */
UPDATE google.appengine.apps
SET 
dispatchRules = '{{ dispatchRules }}',
authDomain = '{{ authDomain }}',
locationId = '{{ locationId }}',
defaultCookieExpiration = '{{ defaultCookieExpiration }}',
servingStatus = '{{ servingStatus }}',
serviceAccount = '{{ serviceAccount }}',
iap = '{{ iap }}',
databaseType = '{{ databaseType }}',
featureSettings = '{{ featureSettings }}',
generatedCustomerMetadata = '{{ generatedCustomerMetadata }}'
WHERE 
appsId = '{{ appsId }}';
```
