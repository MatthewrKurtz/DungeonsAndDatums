package com.dungeonsanddatums.dungeonsanddatums;

import android.content.Context;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Spinner;

import com.dungeonsanddatums.dungeonsanddatums.Adapters.CampaignListAdapter;


/**
 * A simple {@link Fragment} subclass.
 * Activities that contain this fragment must implement the
 * {@link Page_CreateCharacter_Background.OnFragmentInteractionListener} interface
 * to handle interaction events.
 * Use the {@link Page_CreateCharacter_Background#newInstance} factory method to
 * create an instance of this fragment.
 */
public class Page_CreateCharacter_Background extends Fragment implements AdapterView.OnItemSelectedListener
{
    static Spinner spinner_Background;
    View rootView;
    ArrayAdapter<CharSequence> adapter_backgroundSpinner;
    private OnFragmentInteractionListener mListener;
    private static final String TAG = CampaignListAdapter.class.getSimpleName();

    public Page_CreateCharacter_Background()
    {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @return A new instance of fragment Page_CreateCharacter_Background.
     */
    // TODO: Rename and change types and number of parameters
    public static Page_CreateCharacter_Background newInstance(String param1, String param2)
    {
        Page_CreateCharacter_Background fragment = new Page_CreateCharacter_Background();
        Bundle args = new Bundle();
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        if (getArguments() != null)
        {

        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState)
    {
        // Inflate the layout for this fragment
        rootView = inflater.inflate(R.layout.page_create_character__background, container, false);

        spinner_Background = (Spinner) rootView.findViewById(R.id.spinner_BackgroundSelect);

        adapter_backgroundSpinner = ArrayAdapter.createFromResource(this.getContext(),R.array.Background_list, android.R.layout.simple_spinner_item);
        adapter_backgroundSpinner.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner_Background.setAdapter(adapter_backgroundSpinner);
        spinner_Background.setOnItemSelectedListener(this);

        String[] menuItems = getResources().getStringArray(R.array.Acolyte_description);

        // set up list view for background description
        ListView listView = (ListView) rootView.findViewById(R.id.lv_bacgroundDescription);

        ArrayAdapter<String> listViewAdapter = new ArrayAdapter<String>(
                getActivity(),android.R.layout.simple_list_item_1,
                menuItems);

        listView.setAdapter(listViewAdapter);

        return rootView;
    }

    // TODO: Rename method, update argument and hook method into UI event
    public void onButtonPressed(Uri uri)
    {
        if (mListener != null)
        {
            mListener.onFragmentInteraction(uri);
        }
    }

    @Override
    public void onAttach(Context context)
    {
        super.onAttach(context);
        if (context instanceof OnFragmentInteractionListener)
        {
            mListener = (OnFragmentInteractionListener) context;
        } else
        {
            throw new RuntimeException(context.toString()
                    + " must implement OnFragmentInteractionListener");
        }
    }

    @Override
    public void onDetach()
    {
        super.onDetach();
        mListener = null;
    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id)
    {
        String optionSelected = parent.getItemAtPosition(position).toString();
        ListView listView = (ListView) rootView.findViewById(R.id.lv_bacgroundDescription);

        // This is what will be shown in the list view
        String[] acololyteItems = getResources().getStringArray(R.array.Acolyte_description);
        String[] charlatanItems = getResources().getStringArray(R.array.Charlatan_description);

        ArrayAdapter<String> listViewAdapter;

        switch(optionSelected)
        {
            case "Acoltyte":
                listViewAdapter = new ArrayAdapter<String>(
                        getActivity(),android.R.layout.simple_list_item_1,
                        acololyteItems);
                listView.setAdapter(listViewAdapter);
                break;
            case "Charlatan":
                listViewAdapter = new ArrayAdapter<String>(
                        getActivity(),android.R.layout.simple_list_item_1,
                        charlatanItems);
                listView.setAdapter(listViewAdapter);
                break;
        }
    }

    @Override
    public void onNothingSelected(AdapterView<?> parent)
    {

    }

    /**
     * This interface must be implemented by activities that contain this
     * fragment to allow an interaction in this fragment to be communicated
     * to the activity and potentially other fragments contained in that
     * activity.
     * <p>
     * See the Android Training lesson <a href=
     * "http://developer.android.com/training/basics/fragments/communicating.html"
     * >Communicating with Other Fragments</a> for more information.
     */
    public interface OnFragmentInteractionListener
    {
        // TODO: Update argument type and name
        void onFragmentInteraction(Uri uri);
    }

    public static String getBackground()
    {
        return spinner_Background.getSelectedItem().toString();
    }
}
