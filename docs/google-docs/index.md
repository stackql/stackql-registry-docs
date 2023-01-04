---
title: google
hide_title: false
hide_table_of_contents: false
keywords:
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
id: google-doc
slug: /providers/google
---
Cloud computing services offered by Google.  
    

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;&nbsp;&nbsp;<b>130</b></span><br />
<span>total methods:&nbsp;<b>4935</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>1470</b></span><br />
<span>total selectable resources:&nbsp;<b>1307</b></span><br />
</div>
</div>

:::

## Installation
```bash
REGISTRY PULL google v23.01.00104;
```

## Authentication
```javascript
{
  "google": {
    /**
      * Type of authentication to use, suported values include: service_account, interactive
      * @type String
      */
    "type": string, 
    /**
      * path to service account key file.
      * @type String
      */
    "credentialsfilepath": string, 
  }
}
```
### Example (Mac/Linux)
```bash

AUTH='{ "google": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$Auth = "{ 'google': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}'
stackql.exe shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/google/accessapproval/">accessapproval</a><br />
<a href="/providers/google/accesscontextmanager/">accesscontextmanager</a><br />
<a href="/providers/google/analyticshub/">analyticshub</a><br />
<a href="/providers/google/apigateway/">apigateway</a><br />
<a href="/providers/google/apigee/">apigee</a><br />
<a href="/providers/google/apigeeregistry/">apigeeregistry</a><br />
<a href="/providers/google/apikeys/">apikeys</a><br />
<a href="/providers/google/appengine/">appengine</a><br />
<a href="/providers/google/artifactregistry/">artifactregistry</a><br />
<a href="/providers/google/baremetalsolution/">baremetalsolution</a><br />
<a href="/providers/google/beyondcorp/">beyondcorp</a><br />
<a href="/providers/google/bigquery/">bigquery</a><br />
<a href="/providers/google/bigqueryconnection/">bigqueryconnection</a><br />
<a href="/providers/google/bigquerydatatransfer/">bigquerydatatransfer</a><br />
<a href="/providers/google/bigqueryreservation/">bigqueryreservation</a><br />
<a href="/providers/google/bigtableadmin/">bigtableadmin</a><br />
<a href="/providers/google/billingbudgets/">billingbudgets</a><br />
<a href="/providers/google/binaryauthorization/">binaryauthorization</a><br />
<a href="/providers/google/certificatemanager/">certificatemanager</a><br />
<a href="/providers/google/cloudasset/">cloudasset</a><br />
<a href="/providers/google/cloudbilling/">cloudbilling</a><br />
<a href="/providers/google/cloudbuild/">cloudbuild</a><br />
<a href="/providers/google/cloudchannel/">cloudchannel</a><br />
<a href="/providers/google/clouddebugger/">clouddebugger</a><br />
<a href="/providers/google/clouddeploy/">clouddeploy</a><br />
<a href="/providers/google/clouderrorreporting/">clouderrorreporting</a><br />
<a href="/providers/google/cloudfunctions/">cloudfunctions</a><br />
<a href="/providers/google/cloudidentity/">cloudidentity</a><br />
<a href="/providers/google/cloudiot/">cloudiot</a><br />
<a href="/providers/google/cloudkms/">cloudkms</a><br />
<a href="/providers/google/cloudprofiler/">cloudprofiler</a><br />
<a href="/providers/google/cloudresourcemanager/">cloudresourcemanager</a><br />
<a href="/providers/google/cloudscheduler/">cloudscheduler</a><br />
<a href="/providers/google/cloudshell/">cloudshell</a><br />
<a href="/providers/google/cloudsupport/">cloudsupport</a><br />
<a href="/providers/google/cloudtasks/">cloudtasks</a><br />
<a href="/providers/google/cloudtrace/">cloudtrace</a><br />
<a href="/providers/google/composer/">composer</a><br />
<a href="/providers/google/compute/">compute</a><br />
<a href="/providers/google/connectors/">connectors</a><br />
<a href="/providers/google/contactcenterinsights/">contactcenterinsights</a><br />
<a href="/providers/google/container/">container</a><br />
<a href="/providers/google/containeranalysis/">containeranalysis</a><br />
<a href="/providers/google/datacatalog/">datacatalog</a><br />
<a href="/providers/google/dataflow/">dataflow</a><br />
<a href="/providers/google/datafusion/">datafusion</a><br />
<a href="/providers/google/datalabeling/">datalabeling</a><br />
<a href="/providers/google/datamigration/">datamigration</a><br />
<a href="/providers/google/datapipelines/">datapipelines</a><br />
<a href="/providers/google/dataplex/">dataplex</a><br />
<a href="/providers/google/dataproc/">dataproc</a><br />
<a href="/providers/google/datastore/">datastore</a><br />
<a href="/providers/google/datastream/">datastream</a><br />
<a href="/providers/google/deploymentmanager/">deploymentmanager</a><br />
<a href="/providers/google/dialogflow/">dialogflow</a><br />
<a href="/providers/google/dlp/">dlp</a><br />
<a href="/providers/google/dns/">dns</a><br />
<a href="/providers/google/documentai/">documentai</a><br />
<a href="/providers/google/domains/">domains</a><br />
<a href="/providers/google/essentialcontacts/">essentialcontacts</a><br />
<a href="/providers/google/eventarc/">eventarc</a><br />
<a href="/providers/google/file/">file</a><br />
<a href="/providers/google/firestore/">firestore</a><br />
<a href="/providers/google/gameservices/">gameservices</a><br />
<a href="/providers/google/genomics/">genomics</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/google/gkebackup/">gkebackup</a><br />
<a href="/providers/google/gkehub/">gkehub</a><br />
<a href="/providers/google/healthcare/">healthcare</a><br />
<a href="/providers/google/iam/">iam</a><br />
<a href="/providers/google/iamcredentials/">iamcredentials</a><br />
<a href="/providers/google/iap/">iap</a><br />
<a href="/providers/google/identitytoolkit/">identitytoolkit</a><br />
<a href="/providers/google/ids/">ids</a><br />
<a href="/providers/google/jobs/">jobs</a><br />
<a href="/providers/google/language/">language</a><br />
<a href="/providers/google/libraryagent/">libraryagent</a><br />
<a href="/providers/google/lifesciences/">lifesciences</a><br />
<a href="/providers/google/logging/">logging</a><br />
<a href="/providers/google/managedidentities/">managedidentities</a><br />
<a href="/providers/google/memcache/">memcache</a><br />
<a href="/providers/google/metastore/">metastore</a><br />
<a href="/providers/google/ml/">ml</a><br />
<a href="/providers/google/monitoring/">monitoring</a><br />
<a href="/providers/google/networkconnectivity/">networkconnectivity</a><br />
<a href="/providers/google/networkmanagement/">networkmanagement</a><br />
<a href="/providers/google/networksecurity/">networksecurity</a><br />
<a href="/providers/google/networkservices/">networkservices</a><br />
<a href="/providers/google/notebooks/">notebooks</a><br />
<a href="/providers/google/ondemandscanning/">ondemandscanning</a><br />
<a href="/providers/google/orgpolicy/">orgpolicy</a><br />
<a href="/providers/google/osconfig/">osconfig</a><br />
<a href="/providers/google/oslogin/">oslogin</a><br />
<a href="/providers/google/policysimulator/">policysimulator</a><br />
<a href="/providers/google/policytroubleshooter/">policytroubleshooter</a><br />
<a href="/providers/google/privateca/">privateca</a><br />
<a href="/providers/google/pubsub/">pubsub</a><br />
<a href="/providers/google/pubsublite/">pubsublite</a><br />
<a href="/providers/google/recaptchaenterprise/">recaptchaenterprise</a><br />
<a href="/providers/google/recommendationengine/">recommendationengine</a><br />
<a href="/providers/google/recommender/">recommender</a><br />
<a href="/providers/google/redis/">redis</a><br />
<a href="/providers/google/resourcesettings/">resourcesettings</a><br />
<a href="/providers/google/retail/">retail</a><br />
<a href="/providers/google/run/">run</a><br />
<a href="/providers/google/runtimeconfig/">runtimeconfig</a><br />
<a href="/providers/google/secretmanager/">secretmanager</a><br />
<a href="/providers/google/securitycenter/">securitycenter</a><br />
<a href="/providers/google/serviceconsumermanagement/">serviceconsumermanagement</a><br />
<a href="/providers/google/servicecontrol/">servicecontrol</a><br />
<a href="/providers/google/servicedirectory/">servicedirectory</a><br />
<a href="/providers/google/servicemanagement/">servicemanagement</a><br />
<a href="/providers/google/servicenetworking/">servicenetworking</a><br />
<a href="/providers/google/serviceusage/">serviceusage</a><br />
<a href="/providers/google/sourcerepo/">sourcerepo</a><br />
<a href="/providers/google/spanner/">spanner</a><br />
<a href="/providers/google/speech/">speech</a><br />
<a href="/providers/google/storage/">storage</a><br />
<a href="/providers/google/storagetransfer/">storagetransfer</a><br />
<a href="/providers/google/texttospeech/">texttospeech</a><br />
<a href="/providers/google/tpu/">tpu</a><br />
<a href="/providers/google/trafficdirector/">trafficdirector</a><br />
<a href="/providers/google/transcoder/">transcoder</a><br />
<a href="/providers/google/translate/">translate</a><br />
<a href="/providers/google/videointelligence/">videointelligence</a><br />
<a href="/providers/google/vision/">vision</a><br />
<a href="/providers/google/vmmigration/">vmmigration</a><br />
<a href="/providers/google/webrisk/">webrisk</a><br />
<a href="/providers/google/websecurityscanner/">websecurityscanner</a><br />
<a href="/providers/google/workflowexecutions/">workflowexecutions</a><br />
<a href="/providers/google/workflows/">workflows</a><br />
</div>
</div>
